# app/logic.py
import spacy
from spacy.matcher import PhraseMatcher

def extract_skills(resume_text: str, nlp):
    programming_skills = ["python", "sql", "java", "c++", "r", "javascript"]
    tools = ["git", "jupyter", "excel", "vscode", "powerbi"]
    roles = ["data scientist", "data analyst", "machine learning engineer"]
    def create_matcher_patterns(words):
        return [nlp.make_doc(text) for text in words]
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

def get_comparison_and_suggestions(resume_text: str, jd_text: str, nlp):
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

def analyze_resume_length(resume_text: str, nlp):
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