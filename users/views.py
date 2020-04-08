from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import UpdateView
from .models import CustomUser

from .forms import CustomUserCreationForm,CustomUserChangeForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



class UserUpdateView(LoginRequiredMixin,UpdateView):
    model = CustomUser
    fields = ('username', 'email', 'mobile_number')
    template_name = 'changepersonalinfo.html'
    success_url = reverse_lazy('success')

def success(request):
    return render(request,'Success.html')
