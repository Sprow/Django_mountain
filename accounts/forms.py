from django import forms
# from django.contrib.auth.forms import UserCreationForm

# from django.contrib.auth.models import User
from accounts.models import User

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=4, max_length=10, widget=forms.TextInput(attrs={"type": "password"}))

class RegistrationForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField()
    password1 = forms.CharField(min_length=4, max_length=10, widget=forms.TextInput(attrs={"type": "password"}))
    password2 = forms.CharField(min_length=4, max_length=10, widget=forms.TextInput(attrs={"type": "password"}))


    # class Meta:
    #     model = User
    #     fields = ('email', 'password1', 'password2')
