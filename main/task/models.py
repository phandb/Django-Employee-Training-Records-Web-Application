from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Task(models.Model):
    task_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    date_taken = models.DateTimeField(default=timezone.now)
    date_expired = models.DateTimeField(default=timezone.now)

    # Define OneToMany Relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name
