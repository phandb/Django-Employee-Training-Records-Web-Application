from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


@login_required()
def home_page(request):
    tasks = Task.objects.filter(user=request.user.id)
    context = {
        'tasks': tasks.order_by('task_name')

    }
    return render(request, 'task/home.html', context)


def about_page(request):
    return render(request, 'task/about.html')


@login_required()
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        form.instance.user = request.user

        if form.is_valid():
            form.save()
            return redirect('task-home')
    else:
        form = TaskForm()

    # tasks = Task.objects.filter(user=request.user.id)
    context = {
        # 'tasks': tasks.order_by('task_name'),
        'form': form
    }
    return render(request, 'task/add-task.html', context)


@login_required()
def edit_task(request, task_id):
    return render(request, 'task/edit-task.html')


@login_required()
def delete_task(request, task_id):
    Task.objects.filter(id=task_id).delete()
    return redirect('task-home')
