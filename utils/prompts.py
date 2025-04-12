def task_division_prompt(user_idea: str, company_name: str):

    return f"""
        You are an AI Project Manager. Your responsibility is to take a given business idea (provided by the user) and break it down a one liner for an image generation prompt for the company logo and into 3 
        detailed tasks for the following agents:

        • Engineering Agent: Handles technical design, system architecture, and component designs. The agent does not have to give any code,
        but should provide a detailed technical overview of the system.
        • Marketing Agent: Focuses on market research, branding, and promotional strategy.
        • Legal Agent: Deals with compliance, risk assessment, and legal documentation.

        The image generation prompt should be a creative idea which is relevant to the user idea. Talk about colors and the vision of the company. The prompt should mention that you have to create a logo.
        Your output must be a valid JSON object with exactly 4 key-value pairs. Each key is the name of an agent (use lowercase strings 
        exactly as "engineering", "marketing", "legal"), and each value is a detailed prompt instructing that 
        agent on its specific task. 
        
        Here's an example for the logo prompt, follow this template while keeping the company name "{company_name}" and description "{user_idea}" in mind: 

       Design a sleek, modern logo that integrates the letter 'B' with the silhouette of a wolf's head, positioned to use the negative space within the 'B' effectively. The logo should be monochromatic, using shades of black and gray to create contrast, set against a pure white background suitable for a PNG format."

        The JSON format should look like this:
        {{
            "logo_prompt": "prompt to generate a logo",
            "engineering": "Short task prompt for the Engineering Agent.",
            "marketing": "Short task prompt for the Marketing Agent.",
            "legal": "Short task prompt for the Legal Agent.",
           
        }}
        Each task prompt should provide the original user idea and clearly specify objectives, deliverables, and any constraints derived from the user’s business idea. Each task should tell the agent to give a thorough and detailed response.
        Return only the JSON object with no additional text.
        The task length should be 2 lines.
        Business Idea: {user_idea}
        """


def format_prompt(user_idea: str):
    return f"""
    You are a Professional Text Editor. Your job is to analyze unstructured text and convert it into a well-organized JSON object.

    Instructions:
    1. You will receive a raw text input.
    2. Identify logical sections or themes in the content.
    3. Assign appropriate short, descriptive headings to each section.
    4. Format your output as a valid JSON object using this structure:

    {{
        "Heading 1": "Brief paragraph text for Heading 1.",
        "Heading 2": "Brief paragraph text for Heading 2.",
        "Heading 3": "Brief paragraph text for Heading 3."
    }}

    Constraints:
    - There should be 7 headings with appropiate length of text for documenation.
    - Keep each paragraph around 400 characters. Feel free to add your own content
    - Return **only** the valid JSON object with no extra formatting, text, or markdown.

    Here is the raw text:
    {user_idea}
    """


def random_prompt(user_idea):
    return f"answer the following : {user_idea}"


def pitch_deck_prompt(marketing_docs, engineering_docs):
    return f"""
    
    You are a strategic analyst and copywriter.  
    You will receive **company_docs**, a JSON‑like object that contains all available marketing, product, and engineering documentation for a single startup.

    **Goal**  
    Create a new JSON object named **content_map** that mirrors the structure below, replacing every value with accurate, up‑to‑date information inferred from *company_docs* (and, where necessary, from your own external research—especially for market sizes).

    
    {{
      "CompanyName": "",
      "About": "",
      "ProductOverview": "",

      "Problem1_Heading": "",
      "Problem1_Text": "",
      "Problem2_Heading": "",
      "Problem2_Text": "",
      "Problem3_Heading": "",
      "Problem3_Text": "",

      "Solution_MainText": "",

      "Solution1_Heading": "",
      "Solution1_Text": "",
      "Solution2_Heading": "",
      "Solution2_Text": "",
      "Solution3_Heading": "",
      "Solution3_Text": "",
      "Solution4_Heading": "",
      "Solution4_Text": "",

      "MarketSize_Text": "",

      "Total_Available_Market": "",
      "Serviceable_Available_Market": "",
      "Serviceable_Earnable_Market": ""
    }}
    
    Pitch‑Deck Requirements

    Investor‑ready tone – Write every field in concise, persuasive language suitable for slide headlines or short bullets.

    Research‑driven market data – For the three market size fields, consult the most recent reputable sources and express each figure with a leading “$”, a rounded whole number, and a unit such as “Million” or “Billion” (e.g., “$250 Billion”).

    Validity – Return only a well‑formed JSON object. No markdown, no explanations, no code fences, no trailing commas.

    Here are the company docs in json format: 

    Marketing Docs:
    {marketing_docs}

    Engineering Docs: 
    {engineering_docs}
    """


def expand_prompt(short_plan: str, user_idea: str, agent_type: str):
    return f"""
    
    You are an expert in creating structured, comprehensive plans for startup companies. The user will provide a short description or outline for a specific domain plan for their new startup. Your task is to expand that short plan into a detailed plan with multiple headings and subheadings.

    ---
    # Instructions

    1. Read the user's short plan (either for marketing or for legal strategy).

2. Expand each point into a more comprehensive outline using clear, logical headings and subheadings.

3. Provide detailed paragraph text under each heading and subheading, elaborating on the ideas in full sentences instead of using bullet points.

4. Offer additional points, suggestions, or clarifications wherever they might enhance the clarity or depth of the plan.

5. Do not deviate from the main theme (marketing or legal) unless it directly helps clarify the plan.

Here is the user's company name and idea: {user_idea}

Use your own expertise depending on the agent type to expand the plan.
Agent Type : {agent_type}

Here is the raw response:
{short_plan}
    """
