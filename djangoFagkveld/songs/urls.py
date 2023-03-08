from django.urls import path
from . import views

urlpatterns = [
    path('songs/', views.all_songs, name = 'all-songs'),
    path('songs/<int:song_id>', views.song, name = 'songs'),
    path('', views.all_songs, name = 'all-songs')
]
