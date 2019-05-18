from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from app_base.models import Course
from django.contrib.auth import get_user_model
User = get_user_model()


EDUCATION_TYPES = (
    (0, '---'),
    (1, 'دانش‌آموزش'),
    (2, 'دیپلم'),
    (3, 'دانشجو'),
    (4, 'کاردانی'),
    (5, 'کارشناسی'),
    (6, 'کارشناسی ارشد'),
    (7, 'دکتری'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    _education = models.PositiveSmallIntegerField(choices=EDUCATION_TYPES, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    # birth_date = models.DateField(null=True, blank=True)

    @property
    def education(self):
        return dict(EDUCATION_TYPES)[self._education]

    @education.setter
    def education(self, education_type):
        reversed_types = {v: k for k, v in dict(EDUCATION_TYPES).items()}
        self._education = reversed_types.get(education_type)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if not instance.profile._education:
        instance.profile._education = 0
    instance.profile.save()


class RegisteredCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.user.username, self.course.title)
