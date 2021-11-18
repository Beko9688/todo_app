from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = TaskForm()

    context = {'tasks': tasks, 'form': form}
    return render(request, 'todoapp/index.html', context)


def updateTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    # task = Task.objects.get(id=pk)
    task.delete()
    form = TaskForm(instance=task)
    if request.method == 'POST':

        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')


    return render(request, 'todoapp/update_task.html', {'form': form})


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    item.delete()
    return redirect('homepage')


def strikeTask(request, pk):
    item = Task.objects.get(id=pk)
    if item.complete:
        item.complete = False
        item.save()
    else:
        item.complete = True
        item.save()

    return redirect('homepage')


def delete_all(request):
    Task.objects.all().delete()
    return redirect('homepage')
