from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, UpdateView
from django.contrib import auth, messages
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_GET, require_POST
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.utils import timezone
from metaord.forms import UserForm
from metaord.models import Order, STATUS_CHOICES_AND_CLASS
from metaord.utils.view import ExtraListView
from metaord.utils.auth import Groups
from metaord.utils.decorators import group_required, class_decorator
from chief.forms import ChiefForm
from functools import partial


login_url = reverse_lazy("login")

@group_required("chief", login_url=login_url)
def index(request):
    return render(request, "chief/index.html", {})

@class_decorator(group_required("chief", login_url=login_url))
class OrderList(ExtraListView):
    model = Order
    extra_context = {"statuses": STATUS_CHOICES_AND_CLASS, "status": None}
    template_name = "chief/orders/orders.html"  # todo: chief/orders.html

    def get_context_data(self, **kwargs):
        context = super(OrderList, self).get_context_data(**kwargs)
        self.extra_context["status"] = self.request.GET.get('status')
        context.update(self.extra_context)
        return context

    def get_queryset(self):
        status = self.request.GET.get('status')
        if status is None:
            return Order.objects.all()  
        else: 
            return Order.objects.filter(status=status)

DateInput = partial(forms.DateTimeField, {'class': 'datepicker'})
class OrderUpdate(SuccessMessageMixin, UpdateView):
    model = Order
    template_name = "chief/orders/update.html"
    fields = "__all__"
    success_url = reverse_lazy("chief:orders")
    success_message = "Заказ успешно обновлён"

    def get_context_data(self, **kwargs): # todo: use ExtraView
        context = super(OrderUpdate, self).get_context_data(**kwargs)
        context["pk"] = self.kwargs["pk"] # todo(1.5): pass pk from urls as kwargs (TmplView) 
        return context

class RegistrationView(TemplateView):
    template_name = "chief/register.html"

    def get(self, request, *args, **kwargs):
        super(RegistrationView, self).get(request, args, kwargs)
        user_form = UserForm()
        chief_form = ChiefForm()
        return render(request, self.template_name, {"user_form": user_form, "chief_form": chief_form})

    def post(self, request):
        user_form = UserForm(request.POST)
        chief_form = ChiefForm(request.POST)
        if user_form.is_valid() * chief_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(request.POST.get('password')) # todo: mb cleanded data
            user.save()
            chief = chief_form.save(commit=False)
            chief.user = user
            chief.save()
            user.groups.add(Groups.get_or_create_chief())
            messages.success(request, 'Предпринематель успешно зарегистрирован.')
            return redirect('/chief/', request=request)
        else:
            return render(request, self.template_name, {"user_form": user_form, "chief_form": chief_form})