from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Подтверждение пароля")
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')    
        widgets = {
            'password': forms.PasswordInput(),
        }
