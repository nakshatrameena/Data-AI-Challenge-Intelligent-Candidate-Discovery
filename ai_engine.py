import re

def clean(text):
    return re.sub(r"[^a-zA-Z ]", "", text.lower())

def extract_keywords(text):
    return set(clean(text).split())

def rank_candidates(job_desc, candidates):
    job_keywords = extract_keywords(job_desc)

    results = []

    for c in candidates:
        resume_keywords = extract_keywords(c.resume_text)

        matched = job_keywords.intersection(resume_keywords)
        missing = job_keywords - resume_keywords

        score = len(matched) * 10 + len(resume_keywords) * 0.1

        results.append({
            "id": c.id,
            "name": c.name,
            "score": round(score, 2),
            "matched_skills": list(matched),
            "missing_skills": list(missing),
            "explanation": f"Matched {len(matched)} skills, missing {len(missing)} skills"
        })

    return sorted(results, key=lambda x: x["score"], reverse=True)
