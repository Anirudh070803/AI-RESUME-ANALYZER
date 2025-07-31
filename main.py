import spacy
from spacy.matcher import PhraseMatcher

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

#Function 1: Skill Category Detection

def extract_skills(resume_text):
    programming_skills = ["python", "sql", "java", "c++", "r", "javascript"]
    tools = ["git", "jupyter", "excel", "vscode", "powerbi"]
    roles = ["data scientist", "data analyst", "machine learning engineer"]

    def create_matcher_patterns(words):
        return [nlp.make_doc(text) for text in words]

    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    matcher.add("PROGRAMMING", create_matcher_patterns(programming_skills))
    matcher.add("TOOLS", create_matcher_patterns(tools))
    matcher.add("ROLES", create_matcher_patterns(roles))

    doc = nlp(resume_text)
    matches = matcher(doc)
    categories = {"PROGRAMMING": [], "TOOLS": [], "ROLES": []}

    for match_id, start, end in matches:
        label = nlp.vocab.strings[match_id]
        matched_text = doc[start:end].text.lower()
        if matched_text not in categories[label]:
            categories[label].append(matched_text)

    print("\n📂 Detected Skill Categories:")
    for cat, items in categories.items():
        print(f"{cat}: {', '.join(items) if items else 'None'}")

#Function 2: Resume vs Job Description Matching

def compare_resume_to_jd(resume_text, jd_text):
    resume_doc = nlp(resume_text)
    jd_doc = nlp(jd_text)
    similarity_score = resume_doc.similarity(jd_doc)

    print(f"\n📊 Resume-JD Similarity Score: {similarity_score:.2f} (scale: 0.00 to 1.00)")
    if similarity_score > 0.75:
        print("✅ Good match! Your resume aligns well with the job.")
    elif similarity_score > 0.5:
        print("⚠️ Partial match. Consider adding more relevant keywords.")
        suggest_keywords(resume_text, jd_text)
    else:
        print("❌ Low match. Try tailoring your resume better to the job.")
        suggest_keywords(resume_text, jd_text)
        
#Function 3:

def suggest_keywords(resume_text, jd_text):
    resume_doc = nlp(resume_text)
    jd_doc = nlp(jd_text)

    resume_tokens = {token.lemma_.lower() for token in resume_doc if not token.is_stop and token.is_alpha}
    jd_tokens = {token.lemma_.lower() for token in jd_doc if not token.is_stop and token.is_alpha}

    missing_keywords = jd_tokens - resume_tokens

    # Filter common irrelevant terms
    skip_words = {"experience", "knowledge", "understanding", "ability", "etc", "skills"}
    suggestions = [word for word in missing_keywords if word not in skip_words and len(word) > 3]

    if suggestions:
        print("\n🔍 Suggested Keywords to Add to Your Resume:")
        print(", ".join(sorted(suggestions)[:10]))  # Limit to 10 suggestions
    else:
        print("\n✅ No major keywords missing — your resume covers the JD well!")

#Main Execution

def load_text_from_file(prompt):
    path = input(f"{prompt} (press Enter to skip): ").strip()
    if path:
        try:
            with open(path, "r") as file:
                return file.read()
        except FileNotFoundError:
            print("❌ File not found. Falling back to manual input.")
    return input("Paste text manually:\n")

if __name__ == "__main__":
    print("== AI Resume Analyzer ==")

    resume_text = load_text_from_file("📁 Enter path to resume file")
    extract_skills(resume_text)

    choice = input("\n📝 Want to compare it with a Job Description? (y/n): ").strip().lower()
    if choice == "y":
        jd_text = load_text_from_file("📁 Enter path to JD file")
        compare_resume_to_jd(resume_text, jd_text)

