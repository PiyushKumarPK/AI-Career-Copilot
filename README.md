# AI Career Copilot

I built this project to solve a problem I personally faced — not knowing exactly what skills I was missing for the role I wanted. You upload your resume, tell it your goal, and it tells you where you stand and what to learn next.

It uses Groq's LLaMA model to read your resume and give you a honest breakdown — current skills, gaps, a learning roadmap, and interview questions for that role.

---

## What it does

- Sign up and log in with your account
- Upload your resume as a PDF or DOCX (or just paste the text)
- Enter the role you're targeting — like "Backend Engineer" or "Data Engineer"
- Get back a full analysis: your existing skills, what's missing, a step-by-step roadmap, and interview questions
- View all your past analyses in the History page

---

## Screenshots

| Login | Signup |
|-------|--------|
| ![Login](screenshots/login.png) | ![Signup](screenshots/signup.png) |

| Dashboard | Results |
|-----------|---------|
| ![Dashboard](screenshots/dashboard.png) | ![Results](screenshots/results.png) |

| History |
|---------|
| ![History](screenshots/history.png) |

---

## Tech used

- Python + Flask for the backend
- Groq API (LLaMA 3.3 70B) for the AI analysis
- TiDB Cloud as the database (MySQL-compatible)
- SQLAlchemy for talking to the database
- PyPDF2 and python-docx for reading uploaded resumes
- Plain HTML + CSS for the frontend (no frameworks)

---

## How to run it locally

**Step 1 — Clone the repo**
```
git clone https://github.com/your-username/ai-career-copilot.git
cd ai-career-copilot
```

**Step 2 — Create a virtual environment**
```
python -m venv venv
```

Activate it:
- Windows: `.\venv\Scripts\Activate.ps1`
- Mac/Linux: `source venv/bin/activate`

**Step 3 — Install packages**
```
pip install -r requirements.txt
```

**Step 4 — Set up your environment variables**

Copy the example file:
```
cp .env.example .env
```

Then open `.env` and fill in your keys:
```
GROQ_API_KEY=your_groq_api_key_here
DATABASE_URL=your_tidb_connection_string_here
```

Get a free Groq API key at https://console.groq.com

**Step 5 — Run the app**
```
python app.py
```

Open your browser and go to `http://127.0.0.1:5000`

---

## Environment variables

| Variable | What it's for |
|----------|---------------|
| `GROQ_API_KEY` | Your Groq API key for the AI analysis |
| `DATABASE_URL` | Your TiDB or MySQL connection string |
---

## Project structure

```
ai-career-copilot/
├── app.py              # all the routes
├── ai.py               # resume analysis using Groq
├── db.py               # database connection
├── models.py           # User and Reports tables
├── requirements.txt
├── .env.example
├── static/
│   └── style.css
└── templates/
    ├── base.html
    ├── login.html
    ├── signup.html
    ├── dashboard.html
    └── history.html
```

---

## Notes

- This is a personal project built to practice full stack development with AI integration
- Resume analysis works best when the resume has clear sections and readable text
- Both PDF and DOCX formats are supported for upload
- History page saves all your past analyses so you can track your progress over time

---

Built by Piyush Kumar
