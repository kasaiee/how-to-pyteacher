# Generated by Django 2.1.5 on 2019-04-03 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_base', '0014_auto_20190403_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesession',
            name='video',
            field=models.FileField(null=True, upload_to='private/%Y-%d-%m_%H:%M'),
        ),
    ]
