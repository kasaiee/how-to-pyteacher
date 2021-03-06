# Generated by Django 2.1.5 on 2019-04-03 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_base', '0016_auto_20190403_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseByStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('done', models.BooleanField(default=False)),
                ('rate', models.PositiveSmallIntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='coursesessionexercise',
            name='done',
        ),
        migrations.RemoveField(
            model_name='coursesessionexercise',
            name='rate',
        ),
        migrations.AddField(
            model_name='exercisebystudent',
            name='exercise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_base.CourseSessionExercise'),
        ),
        migrations.AddField(
            model_name='exercisebystudent',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
