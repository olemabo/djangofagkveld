from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

# Create your models here.

class AllSong(models.Model):
    """ Song model """
    title = models.CharField(max_length=30, help_text="title of song")

    song_text = models.TextField(max_length=2000, help_text="the song text")

    release_date = models.DateField(blank=True)

    rating = models.IntegerField(validators=[
        MaxValueValidator(6), MinValueValidator(1)
    ])

    def __str__(self):
        return self.title


    