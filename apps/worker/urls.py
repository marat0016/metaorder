from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^worker/', include('django.contrib.auth.urls')),

    url(r'^worker/register_operator$', views.register_operator_form, name='register_operator_form'),
    url(r'^worker/register_operator_submit$', views.register_operator_submit, name='register_operator_submit'),

    url(r'^orders/$', views.orders_list, name='orders_list'),
    url(r'^order/(?P<order_id>[0-9]+)/$', views.order, name='order'),
]
