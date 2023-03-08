# Generated by Django 3.1.4 on 2023-03-08 14:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='title of song', max_length=30)),
                ('song_text', models.CharField(max_length=2000)),
                ('rating', models.IntegerField(help_text='rating from 1 to 6', validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(1)])),
            ],
        ),
    ]
