from django.shortcuts import render
from .models import Song

# Create your views here.

def index(request):
    songs = Song.objects.all()

    context = {
        "songs": songs,
    }

    return render(request, 'songs/index.html', context)