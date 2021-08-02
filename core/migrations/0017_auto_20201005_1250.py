# Generated by Django 2.2 on 2020-10-05 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20200929_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocode',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='code',
            field=models.CharField(max_length=6),
        ),
        migrations.CreateModel(
            name='UserCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.PromoCode')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Promocodes Used (User)',
            },
        ),
    ]
