from tempfile import template
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from users.forms import  LoginForm, UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.views.generic import CreateView, UpdateView, TemplateView, View, DetailView
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login, authenticate, logout
from django.template import RequestContext
from django.contrib.auth.models import User
from users.models import Profile
from django.urls import reverse
# Create your views here.

class SignUpView(generic.CreateView):
    form_class =  UserRegisterForm
    success_url = reverse_lazy("user:login")
    template_name = "signup.html"

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile) 
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('user:profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile_update.html', context)

class ProfileView(TemplateView):
    template_name = "profile.html"


class LoginPageView(View):
    template_name = 'login.html'
    form_class = LoginForm
    
    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})
        
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('item:item-list')
        message = 'Incorrect Credentials!Please Try again'
        return render(request, self.template_name, context={'form': form, 'message': message})



def log_out(request):
    logout(request)
    return redirect(reverse('user:login'))