from django.shortcuts import render, get_object_or_404
from .models import Worker, Task

def worker_list(request):
    workers = Worker.objects.all()
    return render(request, 'workapp/worker_list.html', {'workers': workers})

def worker_detail(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    tasks = worker.tasks.all()
    return render(request, 'workapp/worker_detail.html', {'worker': worker, 'tasks': tasks})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'workapp/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'workapp/task_detail.html', {'task': task})