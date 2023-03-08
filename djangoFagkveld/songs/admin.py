from django.contrib import admin
from .models import AllSong
# Register your models here.

class AllSongAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating')

admin.site.register(AllSong, AllSongAdmin)