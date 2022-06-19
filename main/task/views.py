from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Task


@login_required()
def home_page(request):
    tasks = Task.objects.filter(user=request.user.id)
    context = {
        'tasks': tasks
    }
    return render(request, 'task/home.html', context)


def about_page(request):
    return render(request, 'task/about.html')


@login_required()
def add_task(request):
    return render(request, 'task/add-task.html')


@login_required()
def edit_task(request):
    return render(request, 'task/edit-task.html')
