from django.shortcuts import get_object_or_404, redirect, render
from .models import Note


def index(request):
    notes = Note.objects.all().order_by("-updated_at")
    return render(request, "core/index.html", {"notes": notes})

def update_note(request):
    if request.method == "POST":
        note_id = request.POST.get("note_id")
        note = get_object_or_404(Note, id=note_id)
        note.title = request.POST.get("title")
        note.content = request.POST.get("content")
        note.save()
        return redirect("index")
    

def create_note(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if title and content:
            Note.objects.create(title=title, content=content)

        return redirect("index")

    return redirect("index")
