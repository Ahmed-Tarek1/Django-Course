from django.urls import path
from . import views

urlpatterns = [
    path("", views.instructors_list, name="instructors_list"),
    path("<int:pk>/", views.instructor_detail, name="instructor_detail"),
]
