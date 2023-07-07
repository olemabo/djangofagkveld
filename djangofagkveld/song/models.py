from django.db import models
from django_mysql.models import ListTextField

# Create your models here.

class Song(models.Model):

    title = models.CharField(max_length=20, help_text="title of song")

    song_text = models.TextField(max_length=2000)

    release_date = models.DateField(blank=True, null=True)

    rating = models.IntegerField()

    def __str__(self):
        return self.title
    

class Participants(models.Model):
    id = models.IntegerField(help_text="Id", primary_key=True)

    name = models.CharField(max_length=30, help_text="name of participant")

    points = ListTextField(
        base_field=models.IntegerField(help_text='Points per game'),
        size=10,  # Maximum of 100 ids in list
    )

    bordtennis = models.IntegerField(help_text='Points for bordtennis', null=True, blank=True)
    fifa = models.IntegerField(help_text='Points for fifa', null=True, blank=True)
    foccia = models.IntegerField(help_text='Points for foccia', null=True, blank=True)
    gulbolle = models.IntegerField(help_text='Points for gulbolle', null=True, blank=True)
    klinkbong = models.IntegerField(help_text='Points for klinkbong', null=True, blank=True)
    bonuspoeng = models.IntegerField(help_text='Points for bonuspoeng', null=True, blank=True)
    kaptein = models.IntegerField(help_text='Points for kaptein', null=True, blank=True)

    def __str__(self):
        return self.name
    

class Tasks(models.Model):
    id = models.IntegerField(help_text="Id", primary_key=True)
    name = models.CharField(max_length=30, help_text="name of task")

    description = models.TextField(help_text='description', null=True, blank=True)
    matches = models.TextField(help_text='matches', null=True, blank=True)
    points = models.TextField(help_text='points', null=True, blank=True)
    
    def __str__(self):
        return self.name