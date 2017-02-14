from django.conf.urls import url
from . import views

app_name = 'dashboard'
urlpatterns = [
    url(r'^user/(?P<user_id>[0-9]+)', views.index, name='index'),
    url(r'^jobdetail/(?P<job_id>[0-9]+)', views.jobdetail, name='jobdetail'),
    url(r'^addjob', views.addjob, name='addjob'),
    url(r'^participate', views.participate, name='participate'),
]
