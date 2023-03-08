from django.urls import path, include
from . import views

urlpatterns = [
    path('songs/', views.index, name='songs'),
    path('songs/<int:song_id>', views.song, name='song')
]
