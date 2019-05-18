from django.contrib import admin
from app_base.models import (
    Course,
    CourseSession,
    CourseSessionExercise,
    ExerciseByStudent,
    AttachmentFiles,
)


class CourseSessionAdmin(admin.ModelAdmin):
    list_filter = ('price', )


admin.site.register(Course)
admin.site.register(CourseSession, CourseSessionAdmin)
admin.site.register(CourseSessionExercise)
admin.site.register(ExerciseByStudent)
admin.site.register(AttachmentFiles)
