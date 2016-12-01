from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import redirect
from django.utils import timezone
from metaord.utils.auth import Permissions, Groups
from metaord.utils.decorators import group_required, class_decorator
from metaord.models import Order
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from metaord.models import Order


login_url = reverse_lazy("login")

@group_required('worker', 'chief', login_url=login_url)
def index(request):
    return render(request, 'worker/index.html', {})

@class_decorator(group_required('worker', 'chief', login_url=login_url))
class OrderList(ListView):
    model = Order
    template_name = "worker/order/orders.html"

@class_decorator(group_required('worker', 'chief', login_url=login_url))
class OrderDetail(DetailView):
    model = Order
    template_name="worker/order/order.html"

@class_decorator(group_required('worker', 'chief', login_url=login_url))
class OrderUpdate(FormView):
    form_class = OrderStatusForm
    template_name = "worker/order/upd_status.html"
    success_url = reverse_lazy("worker:orders") # todo: msg to user

    def form_valid(self, form):        
        order = Order.objects.filter(pk=self.kwargs["pk"])
        assert order is not None
        order.update(status=form.cleaned_data['new_status'])
        return redirect(self.success_url)
    
    def get_context_data(self, **kwargs):
        context = super(OrderUpdate, self).get_context_data(**kwargs)
        context["pk"] = self.kwargs["pk"] # todo(3): pass old status
        return context


@require_GET
@group_required('worker', 'chief', login_url=login_url)
def register_operator_form(request):
    user_form = UserForm()
    oper_form = OperatorForm()
    return render(request, 'registration/register.html', {'user_form': user_form, 'oper_form': oper_form})

@require_POST
@group_required('worker', 'chief', login_url=login_url)
def register_operator_submit(request):
    user_form = UserForm(request.POST)
    oper_form = OperatorForm(request.POST)
    if user_form.is_valid() * oper_form.is_valid(): # todo: why *
        user = user_form.save(commit=False)
        user.set_password(request.POST.get('password'))
        user.save()
        operator = oper_form.save(commit=False)
        operator.user = user
        operator.save()
        user.groups.add(Groups.get_or_create_worker())
        return redirect('/')
    else:
        return render(request, 'registration/register.html', {'user_form': user_form, 'oper_form': oper_form})

