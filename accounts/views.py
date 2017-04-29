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
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("home"))
    else:
        form = RegistrationForm()
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                password1 = data.get('password1')
                password2 = data.get('password2')
                if password1 != password2:
                    # pass_error = ValidationError("Passwords don't match")
                    pass_error = "Passwords don't match"
                    return render(request, 'registration.html', {"form": form, "pass_error": pass_error})
                else:
                    if User.objects.filter(email=data.get("email")):
                        print("User with this email is already exists")
                        return HttpResponseRedirect(reverse("home"))
                    else:
                        user = User.objects.create_user(email=data.get("email"),
                                                        username=data.get("username"))
                        user.set_password(password1)
                        user.save()
                        return HttpResponseRedirect(reverse("login"))
        return render(request, 'registration.html', {"form": form})
