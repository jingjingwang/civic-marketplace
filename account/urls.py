from django.conf.urls import include, url

from . import views

app_name = 'account'
urlpatterns = [
    url(r'login', views.login_view, name='login_view'),
    url(r'logout', views.logout_view, name='logout_view'),
    url(r'register', views.register, name='register'),
    url(r'change', views.change, name='change'),
    url(r'^', views.login_view, name='index'),

]
