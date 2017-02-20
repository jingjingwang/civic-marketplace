from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Job(models.Model):
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()

    def __str__(self):
        return str(self.id)

class Involve(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.participant.id) + '->' + str(self.job.id)

