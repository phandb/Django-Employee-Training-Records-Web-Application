from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='task-home'),
    path('about', views.about_page, name='task-about'),
    path('add-task', views.add_task, name='add-task'),
    path('edit-task', views.edit_task, name='edit-task'),
]
