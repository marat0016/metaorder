from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, FormView
from django.contrib import auth
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import redirect
from django.utils import timezone
from metaord.models import Order
from metaord.utils.decorators import group_required, class_decorator


login_url = reverse_lazy("login")

@group_required("chief", login_url=login_url)
def index(request):
    return render(request, "chief/index.html", {})

@class_decorator(group_required("chief", login_url=login_url))
class OrderList(ListView):
    model = Order
    template_name = "chief/orders/orders.html"  # todo: chief/orders.html
