from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Note

# --- HOME & AUTH VIEWS ---

def home(request):
    return render(request, 'home.html')

def register_user(request):
    if request.method == "POST":
        u = request.POST.get('username')
        e = request.POST.get('email')
        p = request.POST.get('password')
        
        if User.objects.filter(username=u).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')
        
        User.objects.create_user(username=u, email=e, password=p)
        messages.success(request, "Account created! Now you can login.")
        return redirect('login')
    return render(request, 'register.html')

def login_user(request):
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('view_notes')
        else:
            if not User.objects.filter(username=u).exists():
                messages.error(request, "Account doesn't exist.")
            else:
                messages.error(request, "Incorrect password.")
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

# --- PRIVATE NOTES LOGIC ---

@login_required
def view_notes(request):
    query = request.GET.get('q')
    # Sirf login user ke notes
    notes = Note.objects.filter(owner=request.user)
    if query:
        notes = notes.filter(Q(title__icontains=query) | Q(content__icontains=query))
    
    notes = notes.order_by('-pinned', '-created_at')
    return render(request, 'note_list.html', {'notes': notes})

@login_required
def create_note(request):
    if request.method == "POST":
        Note.objects.create(
            owner=request.user,
            title=request.POST.get('title'),
            content=request.POST.get('content'),
            color=request.POST.get('color', '#FFFF99')
        )
        return redirect('view_notes')
    return render(request, 'note_form.html')

@login_required
def edit_note(request, pk):
    note = get_object_or_404(Note, id=pk, owner=request.user)
    if request.method == "POST":
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.color = request.POST.get('color')
        note.save()
        return redirect('view_notes')
    return render(request, 'note_form.html', {'note': note})

@login_required
def delete_note(request, pk):
    note = get_object_or_404(Note, id=pk, owner=request.user)
    note.delete()
    return redirect('view_notes')

@login_required
def toggle_pin(request, pk):
    note = get_object_or_404(Note, id=pk, owner=request.user)
    note.pinned = not note.pinned
    note.save()
    return redirect('view_notes')

