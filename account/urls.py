from django.conf.urls import url
from . import views

app_name = 'account'
urlpatterns = [
    url(r'login', views.login, name='login'),
    url(r'logout', views.logout, name='logout'),
    url(r'register', views.register, name='register'),
    url(r'change', views.change, name='change'),
    url(r'^', views.index, name='index'),
]
