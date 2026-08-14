import fitz

from langchain_ollama import ChatOllama

def extract_text_from_pdf(pdf_file):
    document = fitz.open(
        stream=pdf_file.read(),
        filetype="pdf"
    )

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text

def analyze_job_posting(job_posting):
    llm = ChatOllama(
        model="llama3.2:1b",
        temperature=0
    )

    prompt = f"""
You are a job posting analyzer.

Your task is to identify EVERY technical skill explicitly
required or mentioned in the job posting.

Technical skills include:
- Programming languages such as Python, Java, JavaScript, C#, Go
- Frameworks such as Django, React, Angular, Spring
- Libraries
- Databases
- Cloud platforms
- DevOps tools
- Software development tools
- AI/ML technologies

IMPORTANT:
- If a programming language appears anywhere in the job posting,
  include it as a skill.
- "Python developer" means Python is a required technical skill.
- Do not exclude a technology because it is used as part of a job title.
- Do not infer skills that are not mentioned.
- Include each skill only once.
- Return ALL skills you find.

Return ONLY a comma-separated list of technical skills.
Do not provide explanations.

Job posting:
{job_posting}
"""

    response = llm.invoke(prompt)

    return response.content