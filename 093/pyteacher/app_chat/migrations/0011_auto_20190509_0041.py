# Generated by Django 2.1.5 on 2019-05-08 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('app_chat', '0010_auto_20190504_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='chat',
            name='object_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]