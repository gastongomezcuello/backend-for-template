from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


from users.forms import RegisterForm, ProfileForm
from users.models import UserProfile
from admin_settings.models import Language, Country


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
    logout(request)
    return redirect("login")


def register_view(request):
    if request.method == "GET":

        return render(request, "users/register.html")
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            errors = form.errors
            print(errors)
            context = {
                "errors": errors,
            }
            return render(request, "users/register.html", context)


def users_list_view(request):
    return render(request, "users/users_list.html")


def profile_view(request):

    choices = UserProfile.CHOICE
    availabilities = [choice[0] for choice in choices]

    if request.method == "GET":

        context = {
            "availabilities": availabilities,
            "languages": Language.objects.all(),
            "countries": Country.objects.all(),
        }
        print(context)
        return render(request, "users/profile.html", context=context)
    elif request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
        else:
            errors = form.errors
            context = {
                "errors": errors,
                "languages": Language.objects.all(),
                "countries": Country.objects.all(),
            }
            print(request.POST)
            return render(request, "users/profile.html", context)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
