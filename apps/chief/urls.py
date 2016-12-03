from django.conf.urls import include, url
from django.contrib import admin, auth
from . import views

app_name = "chief"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    url(r'^orders/$', views.OrderList.as_view(), name='orders'),
    url(r'^orders/upd/(?P<pk>[0-9]+)/$', views.OrderUpdate.as_view(), name='order_upd'),

    url(r'^register/$', views.RegistrationView.as_view(), name='register'),
]
