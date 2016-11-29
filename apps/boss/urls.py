from django.conf.urls import include, url
from django.contrib import admin, auth
from . import views


urlpatterns = [
    url(r'^boss/$', views.boss, name='boss'),
]
