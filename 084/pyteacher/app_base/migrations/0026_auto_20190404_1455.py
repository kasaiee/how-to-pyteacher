# Generated by Django 2.1.5 on 2019-04-04 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_base', '0025_auto_20190404_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursesession',
            name='next_session',
        ),
        migrations.AddField(
            model_name='coursesession',
            name='prev_session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prev', to='app_base.CourseSession'),
        ),
        migrations.AlterField(
            model_name='coursesession',
            name='aparat_video',
            field=models.TextField(blank=True, null=True),
        ),
    ]