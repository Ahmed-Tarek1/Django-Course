from django.shortcuts import render
from .models import Course


def courses_list(request):
    courses = Course.objects.all()

    return render(request, "courses/courses_list.html", {
        "courses": courses
    })