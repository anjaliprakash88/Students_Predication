from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserData

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['name', 'place', 'marks', 'class_name', 'semester', 'gender', 'nationality', 'grade', 'section', 'topic', 'stage', 'absent_days']


