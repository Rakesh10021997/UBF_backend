# Generated by Django 2.2 on 2020-09-29 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_merge_20200926_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiztaker',
            name='starttime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
