from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django import forms
from datetime import datetime
from datetimewidget.widgets import DateTimeWidget

from account.models import User, Skill, Cause

class Job(models.Model):
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    identity = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    thumb = models.URLField()
    past = models.BooleanField(default=False)
    def __str__(self):
        return '%s' % (self.title)

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'description', 'location', 'start_time', 'end_time', 'publisher')
        widgets = {
            'start_time': DateTimeWidget(attrs={'id':"start_time"}, usel10n=True, bootstrap_version=3),
            'end_time': DateTimeWidget(attrs={'id':"end_time"}, usel10n=True, bootstrap_version=3),
            'title': forms.Textarea(attrs={'rows': 1}),
            'description': forms.Textarea(attrs={'rows': 5}),
            'publisher': forms.HiddenInput()
        }

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
