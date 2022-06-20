from django import forms

from .models import Task


class TaskForm(forms.ModelForm):

    # create meta class:
    class Meta:
        # specify model to be used
        model = Task

        # specify fields to be used
        fields = ['task_name',
                  'category',
                  'date_taken'
        ]