from app.ai.gemini_client import get_gemini_client

def generate_quick_tips(goal: str) -> str:
    client = get_gemini_client()
    
    prompt = f"Give 3 quick, high-impact tips for someone aiming to achieve: {goal}."
    response = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=prompt,
    )
    return response.text