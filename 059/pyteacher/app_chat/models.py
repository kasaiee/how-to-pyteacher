import jdatetime
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth import get_user_model
User = get_user_model()


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    code = models.TextField(null=True, blank=True)
    message = models.TextField(null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    create_datetime = models.DateTimeField(auto_now_add=True, null=True)
    seen = models.BooleanField(null=True, default=False)
    seen_datetime = models.DateTimeField(null=True)

    def jd_create_datetime(self):
        jdatetime.set_locale('fa_IR')
        jdatetime.datetime.now().strftime('%A %B')
        jd_datetime = jdatetime.datetime.fromgregorian(
            year=self.create_datetime.year,
            month=self.create_datetime.month,
            day=self.create_datetime.day,
            hour=self.create_datetime.hour,
            monute=self.create_datetime.minute,
            second=self.create_datetime.second,
        )
        return jd_datetime.strftime('%A, %d %B %y %H:%M:%S')

    def is_student(self):
        return 'students' in [group.name for group in self.user.groups.all()]

    def is_operator(self):
        return not self.is_student()

    def __str__(self):
        return self.message[:30]
