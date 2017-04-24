from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from accounts.forms import LoginForm, RegistrationForm
from django.core.exceptions import ValidationError
from accounts.models import User


def home_page(request):
    return render(request, "home.html")


@login_required(login_url="/login/")
def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))


def sign_in(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("home"))
    else:
        form = LoginForm()
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = authenticate(email=data.get("email"), password=data.get("password"))
                if user:
                    login(request, user)
                    return HttpResponseRedirect(reverse("home"))
                else:
                    print("sorry")
        return render(request, "login.html", {"form": form})

def registerate_user(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            password1 = data.get('password1')
            password2 = data.get('password2')
            if password1 != password2:
                raise ValidationError("Passwords don't match")
            else:
                user1 = authenticate(email=data.get("email"))
                if user1:
                    print("User with this email is already exists")
                    return HttpResponseRedirect(reverse("home"))
                else:
                    user = User.objects.create_user(email=data.get("email"),
                                                    password=data.get("password1"),
                                                    username=data.get("username"))
                    return HttpResponseRedirect(reverse("login"))
    return render(request, 'registration.html', {"form": form})
