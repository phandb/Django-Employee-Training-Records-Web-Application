from django.shortcuts import render


# Create your views here.

def home_page(request):
    return render(request, 'task/home.html')


def about_page(request):
    return render(request, 'task/about.html')


def add_task(request):
    return render(request, 'task/add-task.html')


def edit_task(request):
    return render(request, 'task/edit-task.html')
