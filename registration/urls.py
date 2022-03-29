from re import template
from django.contrib import admin
from django.urls import path
from registration import views
from django.contrib.auth import views as v
from registration import forms
urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name="register"),
    path('login/', v.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path('reset/', v.PasswordResetView.as_view(template_name="registration/reset.html"), name="reset"),
    path('logout/', v.LogoutView.as_view(), name='logout'),
]
