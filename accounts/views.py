from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.views import View
from .forms import UserCreationForm, UserLoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


def home_view(request):
    return render(request, 'accounts/home.html')

class UserRegisterView(View):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have registered successfully.', 'success')
            return redirect('accounts:home')
        
        messages.error(request, 'Form is not valid.', 'danger') 
        return render(request, self.template_name, {'form':form}) 


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('accounts:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user=user)
            messages.success(request, 'You have logged in successfully')
            return redirect('accounts:home')
        return render(request, self.template_name, {'form':form})


class UserLogOutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You have logged out successfully.', 'success')
        return redirect('accounts:home')
