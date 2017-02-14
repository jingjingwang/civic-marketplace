from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class User(models.Model):
    email = models.CharField(max_length=100)
    display_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)

    #def was_published_recently(self):
    #    now = timezone.now()
    #    return now - datetime.timedelta(days=1) <= self.pub_date <= now
