# Generated by Django 2.1.5 on 2019-04-04 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_accounts', '0012_settings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='show_resume',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Settings',
        ),
    ]
