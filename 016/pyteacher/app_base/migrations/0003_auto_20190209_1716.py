# Generated by Django 2.1.5 on 2019-02-09 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_base', '0002_coursesessionexercise_course_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachmentfiles',
            name='file',
            field=models.FileField(upload_to='attach-files/%y-%m-%d_%H:%M'),
        ),
    ]
