# Generated by Django 3.1.4 on 2023-03-08 15:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0002_auto_20230308_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='release_data',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 3, 8, 16, 17, 0, 411582)),
        ),
    ]