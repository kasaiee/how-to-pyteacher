# Generated by Django 2.1.5 on 2019-04-04 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_base', '0024_auto_20190404_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursesession',
            name='next_session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next', to='app_base.CourseSession'),
        ),
    ]
