from django.db import models
from instructors.models import Instructor

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.CASCADE,
        related_name="courses"
    )
    image = models.ImageField(upload_to="course_images/", blank=True, null=True)  # new field

    def __str__(self):
        return f"{self.name} ({self.code})"