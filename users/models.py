from django.db import models
from django.contrib.auth.models import User

from admin_settings.models import Country, Language


class UserProfile(models.Model):

    CHOICE = (
        ("Full-time", "Full-time"),
        ("Part-time", "Part-time"),
        ("Freelance", "Freelance"),
        ("Other", "Other"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone_number = models.CharField(max_length=24, blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    profile_image = models.ImageField(
        upload_to="profile_images",
        blank=True,
        null=True,
        default="profile_images/default.jpg",
    )
    cover_image = models.ImageField(
        upload_to="cover_images",
        blank=True,
        null=True,
        default="cover_images/default.jpg",
    )
    occupation = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    availability = models.CharField(
        max_length=100, choices=CHOICE, blank=True, null=True
    )
    birthdate = models.DateField(blank=True, null=True)
    years_experience = models.PositiveIntegerField(blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)

    native_language = models.ForeignKey(
        Language, on_delete=models.SET_NULL, blank=True, null=True
    )
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return self.user.username
