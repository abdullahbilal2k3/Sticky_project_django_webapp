from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    # Sirf wahi fields rakhein jo hamare Note model mein hain
    list_display = ('title', 'created_at', 'updated_at', 'color')
    
    # Filter bhi sirf existing fields par lagayein
    list_filter = ('created_at',)
    
    # Search title aur content mein karein
    search_fields = ('title', 'content')