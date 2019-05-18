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

    def __str__(self):
        return self.message[:30]
