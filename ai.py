from groq import Groq
import json
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_resume(resume_text, user_goal):
    prompt = f"""
You are a senior software engineer and hiring manager.
Evaluate the resume based on the user's goal.
User goal: "{user_goal}"

STRICT RULES:
- Extract only relevant skills for this goal
- REMOVE irrelevant tools
- Identify real gaps
- Generate roadmap only for missing skills

IMPORTANT: roadmap must NEVER be empty. For each missing skill, add a learning step.

Return only JSON, no extra text:
{{
    "skills": ["list of current relevant skills"],
    "missing_skills": ["list of skills needed for the goal"],
    "roadmap": [
        "Step 1: Learn X by doing Y",
        "Step 2: Build a project using Z",
        "Step 3: Practice A with B resource"
    ],
    "interview_questions": ["list of interview questions"]
}}

Resume:
{resume_text}
"""
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            messages=[
                {"role": "system", "content": "You are a strict hiring manager. Return only valid JSON."},
                {"role": "user", "content": prompt}
            ]
        )
        content = response.choices[0].message.content.strip()
        start = content.find("{")
        end = content.rfind("}") + 1
        return json.loads(content[start:end])

    except Exception as e:
        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": str(e)
        }