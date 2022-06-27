from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, TaskEditForm


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
        form = TaskForm(request.POST, request=request)
        form.instance.user = request.user

        if form.is_valid():

            form.save()
            return redirect('task-home')
    else:
        form = TaskForm(request=request)

    context = {
        # 'tasks': tasks.order_by('task_name'),
        'form': form
    }
    return render(request, 'task/add-task.html', context)


@login_required()
def edit_task(request, task_id):
    data = Task.objects.get(id=task_id)

    # update_screen = True if update == 'update' else False
    form = TaskEditForm(request.POST or None, request=request)
    if request.method == 'POST':

        if form.is_valid():
            data.task_name = data.task_name
            data.category = data.category
            data.date_taken = form.instance.date_taken
            data.save()
            return redirect('task-home')
    else:
        form_data = {
            'task_name': data.task_name,
            'category': data.category,
            'date_taken': data.date_taken
        }
        form = TaskEditForm(initial=form_data, request=request)

    context = {
        'form': form
    }

    return render(request, 'task/edit-task.html', context)


@login_required()
def delete_task(request, task_id):
    Task.objects.filter(id=task_id).delete()
    return redirect('task-home')
