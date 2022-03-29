from django.shortcuts import render
from django.views.generic import DetailView,CreateView,ListView
from django.contrib.auth.views import PasswordChangeDoneView,PasswordChangeView
from django.urls import reverse_lazy
from django.views import generic
from registration import forms


class UserRegistrationView(generic.CreateView):
    form_class = forms.RegisterForm
    template_name = 'registration/registration.html'
    def get_success_url(self):
        return reverse_lazy('login')

class UserLoginView(generic.CreateView):
    form_class = forms.LoggingForm
    template_name = "registration/login.html"
    def get_success_url(self):
        return reverse_lazy('home')

class UserResetView(generic.CreateView):
    # form_class = forms.ResetForm
    template_name = "registration/reset.html"
    def get_success_url(self):
        return reverse_lazy('home')


