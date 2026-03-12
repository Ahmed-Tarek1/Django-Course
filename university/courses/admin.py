from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "instructor")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100"/>'
        return ""
    image_preview.allow_tags = True

admin.site.register(Course, CourseAdmin)