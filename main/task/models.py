from datetime import datetime, timedelta, timezone
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.timezone import localtime


class Task(models.Model):
    task_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    date_taken = models.DateTimeField(default=datetime.now)
    # date_expired = models.DateTimeField(default=lambda: datetime.now() + timedelta(days=5))

    # Define OneToMany Relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name

    @property
    def date_expired(self):
        return self.date_taken + timedelta(days=5)

    @property
    def days_til_expire(self):
        # Format datetime
        date_format = "%M-%d-%Y"
        # datetime.now() with USE_TZ set to TRUE ia aware datetime.
        # Use localtime(), instead , to get the current time zone.
        days_to_expire = (self.date_expired - localtime()).days

        expired_date = self.date_expired.strftime(date_format)
        today = localtime().strftime(date_format)

        if today < expired_date:
            return str(days_to_expire + 1)
        if today == expired_date:
            return "< 1"
        else:
            return "expired"
