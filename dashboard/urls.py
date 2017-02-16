from django.conf.urls import url
from . import views

app_name = 'dashboard'
urlpatterns = [
    url(r'^jobdetail/(?P<job_id>[0-9]+)', views.jobdetail, name='jobdetail'),
    url(r'^addjob', views.addjob, name='addjob'),
    url(r'^participate', views.participate, name='participate'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^', views.index, name='index'),
]
