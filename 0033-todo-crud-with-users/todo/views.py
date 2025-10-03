from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Task


# Create your views here.
@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, completed=False)
    return render(request, 'todo/tasks.html', {
        "tasks": tasks
        })


@login_required
def new_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description, user=request.user)
        return redirect('todo:tasks')
    return render(request, 'todo/new_task.html')


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'todo/task_detail.html', {
        'task':task
        })


@login_required
def completed_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = True
    task.save()
    return redirect('todo:tasks')

@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        return redirect('todo:tasks')
    return render(request, 'todo/edit_task.html')

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('todo:tasks')