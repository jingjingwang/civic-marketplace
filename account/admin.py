from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserIdentity, Organization, Skill, Cause, UserSkill, UserCause, User

admin.site.register(User)
admin.site.register(UserIdentity)
admin.site.register(Organization)
admin.site.register(Skill)
admin.site.register(Cause)
admin.site.register(UserSkill)
admin.site.register(UserCause)
