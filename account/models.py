from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.URLField(null=True)
    score = models.FloatField(default=0.0, null=True)

class Organization(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    def __str__(self):
        return '%s' % (self.name)

class Skill(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    def __str__(self):
        return '%s' % (self.name)

class Cause(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    def __str__(self):
        return '%s' % (self.name)

class UserIdentity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    identity = models.ForeignKey(Organization, on_delete=models.CASCADE)

class UserSkill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

class UserCause(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE)

class PreferredTime(models.Model):
    name = models.CharField(max_length=50, primary_key=True, default=None)
    def __str__(self):
        return '%s' % (self.name)

class UserPreferredTime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    preferred_time = models.ForeignKey(PreferredTime, on_delete=models.CASCADE)

