import fitz

from langchain_ollama import ChatOllama

OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")

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
        temperature=0,
        base_url=OLLAMA_BASE_URL
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


def analyze_resume(resume_text):
    llm = ChatOllama(
        model="llama3.2:1b",
        temperature=0,
        base_url=OLLAMA_BASE_URL
    )

    prompt = f"""
You are a resume analyzer.

Your task is to identify every technical skill explicitly
mentioned in the resume.

Technical skills include:
- Programming languages such as Python, Java, JavaScript, C#, Go
- Frameworks such as Django, React, Angular, Spring
- Libraries
- Databases
- Cloud platforms
- DevOps tools
- Software development tools
- AI and machine learning technologies

IMPORTANT:
- Only include skills that are explicitly mentioned in the resume.
- Do not infer a skill from a job title.
- Do not infer a skill from a project description unless the technology
  is explicitly mentioned.
- Include programming languages even if they appear in an
  experience or project description.
- Include each skill only once.
- Return all technical skills you can find.

Return ONLY a comma-separated list of technical skills.
Do not provide explanations.

Resume:
{resume_text}
"""

    response = llm.invoke(prompt)

    return response.content