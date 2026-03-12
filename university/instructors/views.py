from django.shortcuts import render
from .models import Instructor

# List all instructors
def instructors_list(request):
    instructors = Instructor.objects.all()
    return render(request, "instructors/instructors_list.html", {
        "instructors": instructors
    })

# Detail page for one instructor
def instructor_detail(request, pk):
    instructor = Instructor.objects.get(pk=pk)
    courses = instructor.courses.all()  # related_name from Course model
    return render(request, "instructors/instructor_detail.html", {
        "instructor": instructor,
        "courses": courses,
    })