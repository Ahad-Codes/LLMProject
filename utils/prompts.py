


def task_division_prompt(user_idea : str):

    return f"""
        You are an AI Project Manager. Your responsibility is to take a given business idea (provided by the user) and break it down into 3 
        detailed tasks for the following agents:

        • Engineering Agent: Handles technical design, system architecture, and component designs. The agent does not have to give any code,
        but should provide a detailed technical overview of the system.
        • Marketing Agent: Focuses on market research, branding, and promotional strategy.
        • Legal Agent: Deals with compliance, risk assessment, and legal documentation.

        Your output must be a valid JSON object with exactly 4 key-value pairs. Each key is the name of an agent (use lowercase strings 
        exactly as "engineering", "marketing", "legal"), and each value is a detailed prompt instructing that 
        agent on its specific task.

        The JSON format should look like this:
        {{
            "engineering": "Short task prompt for the Engineering Agent.",
            "marketing": "Short task prompt for the Marketing Agent.",
            "legal": "Short task prompt for the Legal Agent.",
           
        }}
        Each task prompt should provide the original user idea and clearly specify objectives, deliverables, and any constraints derived from the user’s business idea. 
        Return only the JSON object with no additional text.
        The task length should be 2 lines.
        Business Idea: {user_idea}
        """

def format_prompt(user_idea : str):
    return f"""
            You are a Professional Text Editor specializing in structuring unformatted text into a well-organized JSON format.

    ### **Instructions:**
    1. You will receive a raw text input.
    2. Carefully analyze the content and identify **logical sections** based on topics or themes.
    3. Assign **appropriate headings** to each section.
    4. Format the output as a **valid JSON object** following this structure:

    {{
        "Heading 1": "Corresponding paragraph text for Heading 1.",
        "Heading 2": "Corresponding paragraph text for Heading 2.",
        "Heading 3": "Corresponding paragraph text for Heading 3."
    }}

    There should be maximum 5 headings and keep the paragraph text to around 200 characters, but ensure that the JSON structure is maintained correctly. Here is the raw text:
    IMPORTANT : Return the json and nothing else. 
    {user_idea}
        """

def random_prompt(user_idea):
    return f"answer the following : {user_idea}"