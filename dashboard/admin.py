from django.contrib import admin
from .models import Job, Involve, JobSkill, JobCause

admin.site.register(Job)
admin.site.register(Involve)
admin.site.register(JobCause)
admin.site.register(JobSkill)
