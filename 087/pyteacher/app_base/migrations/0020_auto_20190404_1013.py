# Generated by Django 2.1.5 on 2019-04-04 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_base', '0019_auto_20190404_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercisebystudent',
            name='done_datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='exercisebystudent',
            name='done',
            field=models.BooleanField(default=True),
        ),
    ]
