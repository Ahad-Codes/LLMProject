import json
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx2pdf import convert



def write_docx(data: dict, name, idea):

    doc = Document()
    
    title = doc.add_heading(name, level=1)
    title.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    
    
    doc.add_heading("User Project Idea", level=2)
    doc.add_paragraph(idea)
    
    for agent, responses in data.items():
        doc.add_heading(agent.upper(), level=1)  

        for heading, content in responses.items():

            doc.add_heading(heading, level=2)              
            if isinstance(content, list): 
                for item in content:
                    doc.add_paragraph(f"• {item}", style="List Bullet")
            elif isinstance(content, dict):  
                for key, value in content.items():
                    doc.add_heading(key, level=3)
                    if isinstance(value, list):
                        for sub_item in value:
                            doc.add_paragraph(f"• {sub_item}", style="List Bullet")
                    else:
                        doc.add_paragraph(value)
            else: 
                doc.add_paragraph(content)

    
    docx_filename = r"docs/Project_Documentation.docx"
    doc.save(docx_filename)

    pdf_filename = "Project_Documentation.pdf"
    convert(docx_filename)

    print(f"Document successfully saved as {pdf_filename}.")
