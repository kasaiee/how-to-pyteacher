# Generated by Django 2.1.5 on 2019-02-11 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_accounts', '0002_auto_20190211_1215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='aducation',
            new_name='_education',
        ),
    ]
