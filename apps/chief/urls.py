from django.conf.urls import include, url
from django.contrib import admin, auth
from . import views


urlpatterns = [
    url(r'^chief/$', views.index, name='chief'),
]
