from datetime import datetime, timedelta, timezone
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.timezone import localtime

#
# METHODS = (
#     ('', 'Select ...'),
#     ('EPA_504_1', '504.1'),
#     ('Aroclor', '508.1 Aroclor'),
#     ('Chlordane', '508.1 Chlordane'),
#     ('Pesticides', '508.1 Pesticides'),
#     ('Pesticides_Sublist', '508.1 Pesticides-Sublist'),
#     ('TCEQ_Ind_List', '508.1 TCEQ-Ind-List'),
#     ('Toxaphene', '508.1 Toxaphene'),
#     ('PCB_as_DCB', '508A PCB as DCB'),
#     ('EPA_515_4', '515.4'),
#     ('THM', '524.2 THM'),
#     ('VOC', '524.2 VOC'),
#     ('Endrin', '525.2 Endrin'),
#     ('SOC5', '525.2 SOC5'),
#     ('Carbamates', '531.1 Carbamates'),
#     ('Glyphosate_547', '547 Glyphosate'),
#     ('Glyphosate_548', '548.1 Glyphosate'),
#     ('Endothall', '548.1 Endothall'),
#     ('Para_Diq', '549.2 Para/Diq'),
#     ('HAA', '552.2 HAA')
# )
#
# CATEGORIES = (
#     ('', 'Select ...'),
#     ('Extract', 'Extract'),
#     ('Analysis', 'Analysis'),
#     ('Full Method', 'Full Method')
#
# )


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
