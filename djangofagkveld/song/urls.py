from django.urls import path
from .views import index, song

urlpatterns = [
    path('song/', index, name='songs'),
    path('song/<int:song_id>', song, name='song'),
    path('', index),
]