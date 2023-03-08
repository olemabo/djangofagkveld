from django.urls import path, include
from . import views

urlpatterns = [
    path('songs/', views.index, name='songs')
]
