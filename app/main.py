# app/main.py
import spacy
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import SessionLocal, engine
# We now need all the Pydantic models, let's create a file for them
from . import pydantic_models as schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Resume Analyzer API")
nlp = spacy.load("en_core_web_sm")

# --- CORS Middleware ---
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Dependency for DB session ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Logic Functions ---
# [All your logic functions: extract_skills, get_comparison_and_suggestions, analyze_resume_length go here]
# [No changes are needed to the functions themselves]
def extract_skills(resume_text: str):
    programming_skills = ["python", "sql", "java", "c++", "r", "javascript"]
    tools = ["git", "jupyter", "excel", "vscode", "powerbi"]
    roles = ["data scientist", "data analyst", "machine learning engineer"]
    def create_matcher_patterns(words):
        return [nlp.make_doc(text) for text in words]
    from spacy.matcher import PhraseMatcher
    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    matcher.add("PROGRAMMING", create_matcher_patterns(programming_skills))
    matcher.add("TOOLS", create_matcher_patterns(tools))
    matcher.add("ROLES", create_matcher_patterns(roles))
    doc = nlp(resume_text.lower())
    matches = matcher(doc)
    categories = {"PROGRAMMING": [], "TOOLS": [], "ROLES": []}
    for match_id, start, end in matches:
        label = nlp.vocab.strings[match_id]
        matched_text = doc[start:end].text
        if matched_text not in categories[label]:
            categories[label].append(matched_text)
    return categories

def get_comparison_and_suggestions(resume_text: str, jd_text: str):
    resume_doc = nlp(resume_text)
    jd_doc = nlp(jd_text)
    similarity_score = resume_doc.similarity(jd_doc)
    resume_tokens = {token.lemma_.lower() for token in resume_doc if not token.is_stop and token.is_alpha}
    jd_tokens = {token.lemma_.lower() for token in jd_doc if not token.is_stop and token.is_alpha}
    missing_keywords = jd_tokens - resume_tokens
    skip_words = {"experience", "knowledge", "understanding", "ability", "etc", "skills"}
    suggestions = sorted([word for word in missing_keywords if word not in skip_words and len(word) > 3])[:10]
    return {
        "similarity_score": round(similarity_score, 2),
        "suggested_keywords": suggestions
    }

def analyze_resume_length(resume_text: str):
    doc = nlp(resume_text)
    words = [token.text for token in doc if token.is_alpha]
    word_count = len(words)
    reading_time = round(word_count / 200, 1)
    if word_count < 100:
        assessment = "Resume might be too short."
    elif word_count > 800:
        assessment = "Resume might be too long."
    else:
        assessment = "Resume length is reasonable."
    return {
        "word_count": word_count,
        "estimated_reading_time_minutes": reading_time,
        "assessment": assessment
    }


# --- API Endpoints ---
@app.post("/analyze-skills/", response_model=schemas.AnalysisResponse)
def analyze_resume_skills(request: schemas.ResumeRequest, db: Session = Depends(get_db)):
    detected_skills = extract_skills(request.resume_text)
    db_analysis = models.Analysis(
        analysis_type="skills",
        results={"detected_skills": detected_skills}
    )
    db.add(db_analysis)
    db.commit()
    db.refresh(db_analysis)
    return db_analysis

@app.post("/compare-resume-jd/")
def compare_resume_to_jd(request: schemas.CompareRequest):
    results = get_comparison_and_suggestions(request.resume_text, request.jd_text)
    return {"comparison_results": results}

@app.post("/analyze-length/")
def analyze_length(request: schemas.ResumeRequest):
    results = analyze_resume_length(request.resume_text)
    return {"length_analysis": results}