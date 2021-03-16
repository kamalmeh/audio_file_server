from django.contrib import admin
from .models import Song, Podcast, AudioBook

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    """
    Song Model Admin Configuration for Admin Panel
    """
    list_display = ('name', 'duration', 'uploaded')
    list_display_links = ('name',)
    search_fields = ('name', 'duration')

@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    """
    Song Model Admin Configuration for Admin Panel
    """
    list_display = ('name', 'duration', 'uploaded', 'host', 'participants')
    list_display_links = ('name',)
    search_fields = ('name', 'duration', 'host', 'participants')

@admin.register(AudioBook)
class AudioBookAdmin(admin.ModelAdmin):
    """
    Song Model Admin Configuration for Admin Panel
    """
    list_display = ('title', 'duration', 'uploaded', 'author', 'narrator')
    list_display_links = ('title',)
    search_fields = ('title', 'duration', 'author', 'narrator')
