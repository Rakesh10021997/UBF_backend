# Generated by Django 2.2 on 2020-09-22 05:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20200909_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(1)),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='QuizSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz')),
            ],
            options={
                'verbose_name_plural': 'Quiz Slots',
            },
        ),
    ]
