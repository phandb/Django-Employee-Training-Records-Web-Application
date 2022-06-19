# Generated by Django 4.0.5 on 2022-06-18 02:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_task_date_expired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_expired',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_taken',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
