from django.urls import path
from .views import index, oppgave, oppgaver, lag

urlpatterns = [
    path('results/', index, name='results'),
    path('oppgaver/', oppgaver, name='oppgaver'),
    path('lag/', lag, name='lag'),
    path('oppgaver/<int:oppgave_id>', oppgave, name='oppgave'),
    path('', index),
]