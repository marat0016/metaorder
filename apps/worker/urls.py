from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from . import views
from metaord import views as meta_views

app_name = "worker"
urlpatterns = [
    url(r'^$', views.index, name='worker.index'),

    url(r'^', include('django.contrib.auth.urls')), # todo: registration only

    url(r'^register_operator$', views.register_operator_form, name='register_operator_form'),
    url(r'^register_operator_submit$', views.register_operator_submit, name='register_operator_submit'),

    # todo: templname in classes
    url(r'^orders/$', views.OrderList.as_view(template_name="worker/orders_list.html"), name='orders_list'),
    url(r'^orders/(?P<pk>[0-9]+)/$', views.OrderDetail.as_view(template_name="worker/order.html"), name='order'),
    url(r'^orders/upd_status/(?P<pk>[0-9]+)/$', views.OrderUpdate.as_view(
            template_name="worker/order_upd_status.html", success_url="/worker/orders"), 
        name='order_upd_status'),
]
