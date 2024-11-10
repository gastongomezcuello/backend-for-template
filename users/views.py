from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def login_view(request):
    if request.method == "GET":
        return render(request, "users/login.html")
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")

        else:
            errors = form.errors.get("__all__")
            context = {
                "errors": errors,
            }
            print(errors)
            return render(request, "users/login.html", context)


def logout_view(request):

    return redirect("users/login.html")
