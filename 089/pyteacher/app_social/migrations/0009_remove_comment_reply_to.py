# Generated by Django 2.1.5 on 2019-03-18 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_social', '0008_auto_20190317_1911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='reply_to',
        ),
    ]
