from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=30, help_text='title')
    text = models.CharField(max_length=30)
    music = models.CharField(max_length=30)

    genre = models.CharField(choices=(
            ('v', 'Viser'),
            ('h', 'Hip hop'),
        ), max_length=1
    ) 

    rating = models.IntegerField(
        validators=[MaxValueValidator(6), MinValueValidator(1)])

    def __str__(self):
        return self.title


