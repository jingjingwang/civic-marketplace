from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserSkill, UserCause, UserIdentity, Organization

admin.site.register(UserSkill)
admin.site.register(UserCause)
admin.site.register(UserIdentity)
admin.site.register(Organization)
