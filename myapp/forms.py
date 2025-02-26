from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserData, Teacher

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


# ---------------TEACHER DETAILS ADD FORM--------------
class TeacherForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Teacher
        fields = ['first_name', 'email', 'subject', 'experience', 'phone', 'address']

    def save(self, commit=True):
        teacher = super().save(commit=False)


        if not teacher.user_id:
            user = User.objects.create(
                username=self.cleaned_data['email'],
                first_name=self.cleaned_data['first_name'],
                email=self.cleaned_data['email']
            )
            teacher.user = user

        else:
            teacher.user.first_name = self.cleaned_data['first_name']
            teacher.user.email = self.cleaned_data['email']
            teacher.user.save()

        if commit:
            teacher.save()
        return teacher