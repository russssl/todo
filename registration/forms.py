from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    class Meta:
        model = User
        fields = ("username","first_name","last_name","email","password1","password2")
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = "form-control"
        self.fields['password1'].widget.attrs['class'] = "form-control"
        self.fields['password2'].widget.attrs['class'] = "form-control"
    
class LoggingForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Old Password"}), label="")
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"Old Password"}), label="")
    class Meta:
        model = User
        fields = "__all__"

class ResetForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"New Password"}), label="")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"Repeat New Password"}), label="")
    class Meta:
        model = User
        fields = "__all__"