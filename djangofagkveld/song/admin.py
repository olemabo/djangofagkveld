from django.contrib import admin
from .models import Song, Participants, Tasks
# Register your models here.

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating')

admin.site.register(Song, SongAdmin)
admin.site.register(Participants)
admin.site.register(Tasks)