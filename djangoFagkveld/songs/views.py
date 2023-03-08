from django.shortcuts import render
from .models import AllSong

# Create your views here.

def all_songs(request):
    songs = AllSong.objects.all()

    context = {
        'title': 'Sanger:',
        'songs': songs,
    }

    return render(request, 'songs/songs.html', context)


def song(request, song_id):
    song = AllSong.objects.get(id = song_id)

    context = {
        'song': song
    }

    return render(request, 'songs/song.html', context)