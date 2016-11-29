from django.contrib.auth.models import User
from django import forms
from .models import Operator


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class OperatorForm(forms.ModelForm):
    class Meta:
        model = Operator
        fields = "__all__" 
        exclude = ['user']
