from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.widgets import PasswordInput
from user_app.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta():
        model = User
        fields = ('username','email','password')

class RegForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('portfoliosite','profile_pic')
