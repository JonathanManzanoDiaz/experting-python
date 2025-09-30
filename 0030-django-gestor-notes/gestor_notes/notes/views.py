from datetime import timezone
from django.shortcuts import get_object_or_404, redirect, render
from .models import Note
# Create your views here.

def index(request):
    notes = Note.objects.all().order_by('-updated_at')
    return render(request, 'notes/index.html', {
        'notes': notes,
    })


def create_note(request):
    if request.method == 'POST':
        title = request.note.get('title')
        content = request.note.get('content')
        if title and content:
            Note.objects.create(title=title, content=content)
            return redirect('notes:index')
        else:
            return redirect('notes:create_note')
    return render(request, 'notes/create_note.html')


def note_details(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_details.html', {
        'note': note,
    })

def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if title and content:
            note.title = title
            note.content = content
            note.save()
            return redirect("notes:note_details", pk=note.pk)

    return render(request, "notes/note_edit.html", {
        "note": note,
    })



