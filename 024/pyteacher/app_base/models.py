from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey


def course_image_path(instance, filename):
    return instance.title


class Course(models.Model):
    image = models.ImageField(upload_to=course_image_path, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title

class CourseSession(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    aparat_video = models.TextField(null=True)
    attachment_files = GenericRelation('AttachmentFiles')

    def __str__(self):
        return self.title


class CourseSessionExercise(models.Model):
    course_session = models.ForeignKey(CourseSession, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    attachment_files = GenericRelation('AttachmentFiles')

    def __str__(self):
        return self.title


class AttachmentFiles(models.Model):
    file = models.FileField(upload_to='attach-files/%y-%m-%d_%H:%M')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return self.content_object.title
