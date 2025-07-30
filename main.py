import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Get resume input
resume_text = input("Paste your resume summary: ")

# Process the text
doc = nlp(resume_text)

# Extract keywords: nouns/proper nouns only, filter out short/common ones
keywords = set()
for token in doc:
    if token.pos_ in ("NOUN", "PROPN") and len(token.text) > 2:
        keywords.add(token.text.lower())

# Display keywords
if keywords:
    print("\n🧠 Potential Keywords Detected:")
    print(", ".join(sorted(keywords)))
else:
    print("⚠️ No strong keywords found. Try adding more specific terms.")