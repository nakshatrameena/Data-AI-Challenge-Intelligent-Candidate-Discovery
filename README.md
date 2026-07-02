# AI Recruiter – Intelligent Candidate Discovery

> 🚀 AI-powered candidate ranking and intelligent resume screening system developed for the **Hack2Skill India Runs – Data & AI Challenge**.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-black)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📌 Overview

AI Recruiter is an intelligent candidate discovery system that helps recruiters identify the most suitable candidates by analyzing job descriptions and candidate profiles, calculating relevance scores, and providing explainable rankings.

Unlike traditional Applicant Tracking Systems (ATS) that rely primarily on keyword matching, AI Recruiter evaluates candidates based on skill relevance and produces transparent recommendations that recruiters can easily understand.

---

# 🎯 Problem Statement

Recruiters often receive hundreds of resumes for a single job opening. Manual screening is slow, inconsistent, and traditional ATS systems frequently miss qualified candidates because they depend on exact keyword matches.

This project aims to automate candidate screening by:

- Understanding job descriptions
- Extracting required skills
- Matching candidates against job requirements
- Ranking candidates based on relevance
- Explaining every recommendation

---

# ✨ Features

- Create job postings
- Register candidate profiles
- AI-powered candidate ranking
- Explainable scoring
- REST API
- SQLite database
- Lightweight Flask deployment
- JSON-based responses

---

# ⚙️ Technology Stack

## Backend

- Python 3
- Flask
- Flask-SQLAlchemy

## Database

- SQLite

## AI Engine

- Text preprocessing
- Keyword extraction
- Skill matching
- Explainable scoring algorithm

---

# 📂 Project Structure

```
ai-recruiter/
│
├── app.py
├── models.py
├── ai_engine.py
├── requirements.txt
├── uploads/
└── instance/
```

---

# 🧠 AI Ranking Workflow

```
Recruiter
      │
      ▼
Create Job Description
      │
      ▼
Candidate Profiles
      │
      ▼
AI Engine
      │
      ├── Extract Keywords
      ├── Compare Skills
      ├── Calculate Score
      └── Generate Explanation
      │
      ▼
Ranked Candidate List
```

The ranking engine:

- Extracts keywords from job descriptions
- Extracts keywords from candidate resumes
- Identifies matching skills
- Calculates a relevance score
- Ranks candidates
- Returns matched skills, missing skills, and explanations

---

# 🌐 API Endpoints

## Home

```
GET /
```

Returns application status.

---

## Health Check

```
GET /health
```

Response

```json
{
  "status": "healthy"
}
```

---

## Create Job

```
POST /jobs
```

Example Request

```json
{
  "title": "Python Developer",
  "description": "python flask api sql backend"
}
```

---

## List Jobs

```
GET /jobs
```

---

## Create Candidate

```
POST /candidates
```

Example Request

```json
{
  "name": "Amit",
  "resume_text": "python flask api sql backend"
}
```

---

## List Candidates

```
GET /candidates
```

---

## Rank Candidates

```
GET /rank/<job_id>
```

Example Response

```json
{
  "job_title": "Python Developer",
  "total_candidates": 2,
  "rankings": [
    {
      "id": 1,
      "name": "Amit",
      "score": 40.5,
      "matched_skills": [
        "python",
        "flask",
        "api",
        "sql"
      ],
      "missing_skills": [],
      "explanation": "Matched 4 skills, missing 0 skills"
    }
  ]
}
```

---

# 🚀 Installation

## Clone the repository

```bash
git clone https://github.com/nakshatrameena/Data-AI-Challenge-Intelligent-Candidate-Discovery.git
```

## Move into the project directory

```bash
cd Data-AI-Challenge-Intelligent-Candidate-Discovery
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the application

```bash
python app.py
```

The server starts at:

```
http://127.0.0.1:5000
```

---

# 💻 Example Workflow

## 1. Create a Job

```bash
curl -X POST http://127.0.0.1:5000/jobs \
-H "Content-Type: application/json" \
-d '{"title":"Python Developer","description":"python flask api sql backend"}'
```

---

## 2. Add a Candidate

```bash
curl -X POST http://127.0.0.1:5000/candidates \
-H "Content-Type: application/json" \
-d '{"name":"Amit","resume_text":"python flask api sql backend"}'
```

---

## 3. Get Candidate Ranking

```bash
curl http://127.0.0.1:5000/rank/1
```

---

# 📈 Future Enhancements

- Semantic embeddings for better skill matching
- Resume PDF parsing
- Transformer-based candidate recommendations
- Recruiter dashboard
- Authentication & role-based access
- Analytics dashboard
- Hiring insights
- Vector database integration
- Large Language Model (LLM) support

---

# 🎯 Impact

AI Recruiter demonstrates how Artificial Intelligence can improve recruitment by:

- Reducing resume screening time
- Improving candidate selection quality
- Providing transparent ranking decisions
- Supporting recruiters with explainable recommendations
- Simplifying hiring workflows

---

# 👥 Team

**Project:** AI Recruiter – Intelligent Candidate Discovery

Developed for the **Hack2Skill India Runs – Data & AI Challenge**.

**Team Leader:** Nakshatra Meena

Repository:
https://github.com/nakshatrameena/Data-AI-Challenge-Intelligent-Candidate-Discovery

---

# 📄 License

This project is released under the **MIT License**.

---

# 🙏 Acknowledgements

- Hack2Skill
- Python Community
- Flask Community
- Open Source Contributors

---

# ⭐ Thank You

Thank you for your time and consideration.

**AI Recruiter – Intelligent Candidate Discovery**
