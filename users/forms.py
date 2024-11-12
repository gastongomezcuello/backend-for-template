from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models import UserProfile


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "phone_number",
            "facebook",
            "profile_image",
            "cover_image",
            "occupation",
            "description",
            "availability",
            "birthdate",
            "years_experience",
            "address",
            "company_name",
            "native_language",
            "country",
        ]
