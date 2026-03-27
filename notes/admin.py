from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'pinned', 'created_at', 'color')
    list_filter = ('pinned', 'created_at')
    search_fields = ('title', 'content')