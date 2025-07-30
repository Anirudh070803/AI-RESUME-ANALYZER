import spacy
from spacy.matcher import PhraseMatcher

# Load model
nlp = spacy.load("en_core_web_sm")

# Sample skill categories
programming_skills = ["python", "sql", "java", "c++", "r", "javascript"]
tools = ["git", "jupyter", "excel", "vscode", "powerbi"]
roles = ["data scientist", "data analyst", "machine learning engineer"]

# Convert to spaCy docs
def create_matcher_patterns(words):
    return [nlp.make_doc(text) for text in words]

# Setup matcher
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
matcher.add("PROGRAMMING", create_matcher_patterns(programming_skills))
matcher.add("TOOLS", create_matcher_patterns(tools))
matcher.add("ROLES", create_matcher_patterns(roles))

# Get resume input
resume_text = input("Paste your resume summary: ")
doc = nlp(resume_text)

# Match!
matches = matcher(doc)
categories = {"PROGRAMMING": [], "TOOLS": [], "ROLES": []}

for match_id, start, end in matches:
    label = nlp.vocab.strings[match_id]
    matched_text = doc[start:end].text
    if matched_text.lower() not in categories[label]:
        categories[label].append(matched_text.lower())

# Display results
print("\n📂 Detected Categories:")
for cat, items in categories.items():
    print(f"{cat}: {', '.join(items) if items else 'None'}")