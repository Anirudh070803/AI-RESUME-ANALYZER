resume_text = input("Paste your resume summary: ")

keywords = []

if "Python" in resume_text:
    keywords.append("Python")
if "Machine Learning" in resume_text:
    keywords.append("Machine Learning")
if "Data Science" in resume_text:
    keywords.append("Data Science")

if keywords:
    print("Great! Your resume mentions:", ", ".join(keywords))
else:
    print("Consider adding more relevant keywords.")
