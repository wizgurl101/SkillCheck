from django.http import JsonResponse

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

    return JsonResponse({
        "message": "Received successfully",
        "job_posting": job_posting,
        "resume_filename": resume.name,
        "resume_size": resume.size,
    })
