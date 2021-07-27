from django.shortcuts import render, redirect
from classbook_core.forms import SignUpForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.decorators import login_required // Leon: we should use this decorator in the future.

def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("sign_in") # TODO: change the redirect to the profile page / homepage

        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")

    form = SignUpForm
    return render(request=request, template_name="users/sign_up.html", context={"sign_up_form": form})


def sign_in(request):
    sign_in_successful = False

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                sign_in_successful = True
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('index')

        if not sign_in_successful:
            messages.error(request, 'Invalid username or password.')
            return redirect('sign_in')

    form = AuthenticationForm()
    return render(request=request, template_name='users/sign_in.html', context={'sign_in_form': form})
