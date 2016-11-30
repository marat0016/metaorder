from django.conf.urls import include, url
from django.contrib import admin, auth
from . import views


urlpatterns = [
    url(r'^$', views.index, name='chief'),
    # url(r'^chief/$', views.index, name='chief.soemthing'),
]
