from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms
from datetime import datetime

class UploadFileForm(forms.Form):
    file = forms.FileField()

class Job(models.Model):
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    identity = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    #time = models.DateTimeField(default=timezone.now, blank=True)
    time = models.CharField(max_length=50)
    thumb = models.URLField()
    def __str__(self):
        return '%s' % (self.title)

class Involve(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

class Skill(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return '%s' % (self.name)

class Cause(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return '%s' % (self.name)

class JobSkill(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

class JobCause(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE)


