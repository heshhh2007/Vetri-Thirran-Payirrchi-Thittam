from app.ai.gemini_client import get_gemini_client

def generate_base_plan(name: str, age: int, goal: str, diet: str) -> str:
    client = get_gemini_client()
    
    prompt = f"""
    Create a detailed, personalized weekly workout and diet plan for {name}.
    - Age: {age}
    - Goal: {goal}
    - Dietary Preference: {diet}
    
    Format output cleanly with distinct sections for Workouts and Nutrition.
    """
    
    response = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=prompt,
    )
    return response.text

generate_workout_plan = generate_base_plan