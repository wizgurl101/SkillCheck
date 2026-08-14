from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .services import (
    extract_text_from_pdf,
    analyze_job_posting,
    analyze_resume
)

@csrf_exempt
def skill_check(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST requests are allowed"},
            status=405
        )

    job_posting = request.POST.get("job_posting")
    resume = request.FILES.get("resume")

    if not job_posting:
        return JsonResponse(
            {"error": "job_posting is required"},
            status=400
        )

    if not resume:
        return JsonResponse(
            {"error": "resume is required"},
            status=400
        )

    resume_text = extract_text_from_pdf(resume)
    resume_skills = analyze_resume(resume_text)
    resume_skills_list = resume_skills.split(", ")
    
    skills = analyze_job_posting(job_posting)
    required_skills_list = skills.split(", ")
    
    missing_skills = [
    skill
    for skill in required_skills_list
    if skill not in resume_skills_list
]

    return JsonResponse({
        "missing skills": missing_skills 
    })
