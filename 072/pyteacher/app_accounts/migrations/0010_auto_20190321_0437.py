# Generated by Django 2.1.5 on 2019-03-21 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_base', '0011_auto_20190302_2010'),
        ('app_accounts', '0009_auto_20190316_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeredcourse',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_base.CourseSession'),
        ),
        migrations.AlterField(
            model_name='registeredcourse',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_base.Course'),
        ),
    ]
