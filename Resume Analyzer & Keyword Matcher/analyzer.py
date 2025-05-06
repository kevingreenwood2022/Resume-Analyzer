import re

def extract_keywords(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return set(words)

def compare_texts(resume, job_desc):
    resume_words = extract_keywords(resume)
    job_words = extract_keywords(job_desc)

    matched = resume_words & job_words
    missing = job_words - resume_words
    score = round((len(matched) / len(job_words)) * 100, 2) if job_words else 0

    return {
        "score": score,
        "matched": sorted(matched),
        "missing": sorted(missing)
    }