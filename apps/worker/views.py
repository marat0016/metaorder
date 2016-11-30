from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import redirect
from django.utils import timezone
from metaord.utils.auth import Permissions, Groups
from metaord.utils.decorators import group_required
from metaord.models import Order
from .forms import UserForm, OperatorForm


login_url = '/login/'

@group_required('worker', login_url=login_url)
def index(request):
    return render(request, 'worker/index.html', {})

@group_required('worker', login_url=login_url)
def orders_list(request):
    orders = Order.objects.filter(post_date__lte=timezone.now()).order_by('post_date')
    return render(request, 'worker/orders_list.html', {'orders': orders})

@group_required('worker', login_url=login_url)
def order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'worker/order.html', {'order': order})

@require_GET
@group_required('worker', login_url=login_url)
def register_operator_form(request):
    user_form = UserForm()
    oper_form = OperatorForm()
    return render(request, 'registration/register_operator.html', {'user_form': user_form, 'oper_form': oper_form})

@require_POST
@group_required('worker', login_url=login_url)
def register_operator_submit(request):
    user_form = UserForm(request.POST)
    oper_form = OperatorForm(request.POST)
    if user_form.is_valid() * oper_form.is_valid():
        user = user_form.save(commit=False)
        user.set_password(request.POST.get('password'))
        user.save()
        operator = oper_form.save(commit=False)
        operator.user = user
        operator.save()
        user.groups.add(Groups.get_or_create_worker())
        return redirect('/')
    else:
        return render(request, 'registration/register_operator.html', {'user_form': user_form, 'oper_form': oper_form})

