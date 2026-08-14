from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .services import (
    extract_text_from_pdf,
    analyze_job_posting
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
    
    skills = analyze_job_posting(job_posting)

    return JsonResponse({
        "message": "Resume processed successfully",
        "job_posting": job_posting,
        "resume_filename": resume.name,
        "job_posting_skills": skills
    })
