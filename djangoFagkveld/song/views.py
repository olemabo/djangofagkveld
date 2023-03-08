from django.shortcuts import render
from .models import Song

# Create your views here.

def index(request):
    songs = Song.objects.all()

    context = {
        "songs": songs,
    }

    return render(request, 'song/index.html', context)


def song(request, song_id):
    song = Song.objects.get(id=song_id)

    context = {
        "song": song
    }

    return render(request, 'song/song.html', context)