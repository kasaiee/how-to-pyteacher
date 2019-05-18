from django.contrib import admin
from app_base.models import (
    Course,
    CourseSession,
    CourseSessionExercise,
    ExerciseByStudent,
    AttachmentFiles,
)
from genericadmin.admin import GenericAdminModelAdmin, GenericTabularInline


class AttachmentsInline(GenericTabularInline):
    model = AttachmentFiles


class CourseSessionAdmin(GenericAdminModelAdmin):
    list_filter = ('price', )
    inlines = [
        AttachmentsInline,
    ]


class CourseSessionExerciseAdmin(GenericAdminModelAdmin):
    inlines = [
        AttachmentsInline,
    ]


admin.site.register(Course)
admin.site.register(CourseSession, CourseSessionAdmin)
admin.site.register(CourseSessionExercise, CourseSessionExerciseAdmin)
admin.site.register(ExerciseByStudent)
admin.site.register(AttachmentFiles)
