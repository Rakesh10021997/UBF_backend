# Generated by Django 2.1.5 on 2020-04-22 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiztaker',
            name='date_finished',
            field=models.DateTimeField(null=True),
        ),
    ]
