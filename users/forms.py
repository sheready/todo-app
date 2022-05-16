from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    

    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2', )


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    

    class Meta: 
        model = Profile
        fields = ['image', 'bio']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)

   