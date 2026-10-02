from app.ai.gemini_client import get_gemini_client

def update_existing_plan(current_plan: str, feedback: str) -> str:
    client = get_gemini_client()
    
    prompt = f"""
    Original Fitness Plan:
    {current_plan}
    
    User Adjustment Request:
    {feedback}
    
    Please output an updated plan incorporating this feedback.
    """
    response = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=prompt,
    )
    return response.text