from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django import forms
from datetime import datetime

from account.models import User, Skill, Cause

class UploadFileForm(forms.Form):
    file = forms.FileField()

class Job(models.Model):
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    identity = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    #time = models.DateTimeField(default=timezone.now, blank=True)
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)
    thumb = models.URLField()
    past = models.BooleanField(default=False)
    def __str__(self):
        return '%s' % (self.title)

class Involve(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    review = models.TextField(default='')
    score = models.PositiveSmallIntegerField(default=0)

class JobSkill(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

class JobCause(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE)
