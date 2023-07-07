# Generated by Django 4.1.7 on 2023-07-06 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0003_participants_bonuspoeng_participants_bordtennis_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.IntegerField(help_text='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='name of task', max_length=30)),
                ('description', models.CharField(blank=True, help_text='description', max_length=400, null=True)),
                ('matches', models.CharField(blank=True, help_text='matches', max_length=400, null=True)),
                ('points', models.CharField(blank=True, help_text='points', max_length=400, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='participants',
            name='id',
            field=models.IntegerField(help_text='Id', primary_key=True, serialize=False),
        ),
    ]
