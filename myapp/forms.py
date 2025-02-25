from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserData

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['name', 'place', 'marks', 'class_name', 'semester', 'gender', 'nationality', 'grade', 'section', 'topic', 'stage', 'absent_days']


