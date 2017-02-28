from django.conf.urls import url
from . import views

app_name = 'dashboard'
urlpatterns = [
    url(r'^jobdetail/(?P<job_id>[0-9]+)', views.jobdetail, name='jobdetail'),
    url(r'^addjob', views.addjob, name='addjob'),
    url(r'^managejobs', views.managejobs, name='managejobs'),
    url(r'^manage_one_job/(?P<job_id>[0-9]+)', views.manage_one_job, name='manage_one_job'),
    url(r'^participate', views.participate, name='participate'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^review', views.review, name='review'),
    url(r'^user/(?P<user_id>[0-9]+)', views.public_profile, name='user'),
    url(r'^', views.index, name='index'),
]
