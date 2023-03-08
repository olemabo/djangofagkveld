from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime    

# Create your models here.

class Song(models.Model):
    title = models.CharField(help_text='title of song', max_length=30)

    song_text = models.TextField(max_length=2000)

    rating = models.IntegerField(help_text='rating from 1 to 6', validators=[
        MaxValueValidator(6), MinValueValidator(1)
    ])

    release_data = models.DateField(blank=True, default=datetime.now())

    def __str__(self):
        return self.title