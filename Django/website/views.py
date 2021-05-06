from django.shortcuts import render, redirect
from website.models import AppUser
from website.forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


def homepage(request):
    return render(request, 'website/homepage/homepage.html')


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            appUser = AppUser()
            appUser.user = user
            appUser.save()

            login(request, appUser.user)
            messages.success(request, "Registration successful.")
            return redirect("sign_in")

        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")

    form = SignUpForm
    return render(request=request, template_name="website/users/sign_up.html", context={"sign_up_form": form})


def sign_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("landing")
            else:
                messages.error(request, "Invalid username or password.")

        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    return render(request=request, template_name="website/users/sign_in.html", context={"sign_in_form": form})
