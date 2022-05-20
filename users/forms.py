from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from users.models import Person, Profile
from django.contrib.auth import get_user_model
User = get_user_model()

class UserRegisterForm(BaseUserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    phone = forms.CharField(max_length=20, required=True, help_text='Phone number that will receive OTP')

    class Meta:
        model = Person
        fields = ('username', 'email','phone','password1', 'password2', )


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Person
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    

    class Meta: 
        model = Profile
        fields = ['image', 'bio']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)
    

class VerifyForm(forms.Form):
    code = forms.CharField(max_length=8, required=True, help_text='Enter Code')
