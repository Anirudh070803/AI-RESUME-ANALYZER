import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Get resume input
resume_text = input("Paste your resume summary: ")

# Process the text
doc = nlp(resume_text)

# Extract keywords (nouns and proper nouns)
keywords = [token.text for token in doc if token.pos_ in ("NOUN", "PROPN")]

print("\n🧠 Extracted Keywords:")
print(", ".join(set(keywords)))