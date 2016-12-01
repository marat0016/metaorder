from django.contrib.auth.models import User
from django import forms
from .models import Operator
from metaord.models import Order


class OperatorForm(forms.ModelForm):
    class Meta:
        model = Operator
        fields = "__all__" 
        exclude = ['user']

class OrderStatusForm(forms.Form):
    new_status = forms.CharField(max_length=128)
