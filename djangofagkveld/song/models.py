from django.db import models

# Create your models here.

class Song(models.Model):

    title = models.CharField(max_length=20, help_text="title of song")

    song_text = models.TextField(max_length=2000)

    release_date = models.DateField(blank=True, null=True)

    rating = models.IntegerField()

    def __str__(self):
        return self.title