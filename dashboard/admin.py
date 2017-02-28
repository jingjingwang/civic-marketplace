from django.contrib import admin
from .models import Job, Involve, Skill, Cause, JobSkill, JobCause

admin.site.register(Job)
admin.site.register(Involve)
admin.site.register(Skill)
admin.site.register(Cause)
admin.site.register(JobCause)
admin.site.register(JobSkill)
