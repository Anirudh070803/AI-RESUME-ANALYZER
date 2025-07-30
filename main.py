resume_text = input("Paste your resume summary: ")

if "Python" in resume_text:
    print("Great! Your resume mentions Python.")
elif "Data Science" in resume_text:
    print("Nice! You're aligned with Data Science.")
else:
    print("Consider adding more relevant keywords.")