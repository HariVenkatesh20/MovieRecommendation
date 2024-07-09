
from django import forms
from .models import UserRegister

'''class UserForm(forms.ModelForm):
    class Meta:
        model = UserRegister
        fields = ['username', 'email', 'password']'''


class LoginForm(forms.ModelForm):
    class Meta:
        model = UserRegister
        fields = ['username', 'password']



class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserRegister
        fields = ['username', 'email', 'password']