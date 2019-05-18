from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey


def course_image_path(instance, filename):
    return instance.title

def attachment_path(instance, filename):
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

    def get_absolute_url(self):
        params = {'course_id': self.course.id, 'session_id': self.id}
        return reverse('app-base:course-session-detail', kwargs=params)

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

    @property
    def title(self):
        return self.file.url.split('/')[-1]

    @property
    def color(self):
        colors = {
            'ppt': 'orange',
            'pptx': 'orange',
            'doc': 'light-blue darken-3',
            'docx': 'light-blue darken-3',
            'csv': 'green',
            'xlsx': 'green',
            'xls': 'green',
            'py': 'yellow',
            'pdf': 'pink',
        }
        file_format = self.title.split('.')[-1]
        return colors.setdefault(file_format, 'grey')

    def __str__(self):
        return self.content_object.title
