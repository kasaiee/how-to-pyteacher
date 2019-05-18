from django.contrib import admin
from app_base.models import (
    Course,
    CourseSession,
    CourseSessionExercise,
    AttachmentFiles,
)

admin.site.register(Course)
admin.site.register(CourseSession)
admin.site.register(CourseSessionExercise)
admin.site.register(AttachmentFiles)