resume_text = input("Paste your resume summary: ").lower()

keywords = {
    "python": "Python",
    "machine learning": "Machine Learning",
    "data science": "Data Science"
}

found = []

for key in keywords:
    if key in resume_text:
        found.append(keywords[key])

if found:
    print("Great! Your resume mentions:", ", ".join(found))
else:
    print("Consider adding more relevant keywords.")