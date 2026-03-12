from django.shortcuts import render
from .models import Student


def students_list(request):
    students = Student.objects.all()

    return render(request, "students/students_list.html", {
        "students": students
    })