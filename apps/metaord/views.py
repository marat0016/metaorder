from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from metaord.models import Order


class OrderList(ListView):
    model = Order

class OrderDetail(DetailView):
    model = Order

class OrderCreate(CreateView):
    model = Order
    fields = "__all__"

class OrderDelete(DeleteView):
    model = Order
    success_url = '/deleted'