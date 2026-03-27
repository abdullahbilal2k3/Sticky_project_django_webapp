from django.shortcuts import render, redirect, get_object_or_404
from .models import Note

def home(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        Note.objects.create(title=title, content=content)
        return redirect('home')
    
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'notes': notes})

def delete_note(request, pk):
    note = get_object_or_404(Note, id=pk)
    note.delete()
    return redirect('home')

def edit_note(request, pk):
    note = get_object_or_404(Note, id=pk)
    if request.method == "POST":
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('home')
    return render(request, 'edit_note.html', {'note': note})