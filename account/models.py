from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from dashboard.models import Skill, Cause

class Organization(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return '%s' % (self.name)

class UserSkill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

class UserCause(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE)

class UserIdentity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    identity = models.ForeignKey(Organization, on_delete=models.CASCADE)
