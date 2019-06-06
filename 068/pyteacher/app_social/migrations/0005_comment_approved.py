# Generated by Django 2.1.5 on 2019-03-15 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_social', '0004_comment_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(choices=[(False, 'تائید نشده'), (True, 'تائید شده')], default=False, null=True),
        ),
    ]