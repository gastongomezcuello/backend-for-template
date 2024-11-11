from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    CHOICE = (
        ("full-time", "full-time"),
        ("part-time", "part-time"),
        ("freelance", "freelance"),
        ("other", "other"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone_number = models.CharField(max_length=24, blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="profile_pictures", blank=True, null=True
    )
    cover_picture = models.ImageField(upload_to="cover_pictures", blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    availability = models.CharField(
        max_length=100, choices=CHOICE, blank=True, null=True
    )
    birth_date = models.DateField(blank=True, null=True)
    years_experience = models.PositiveIntegerField(blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)

    # language
    # country

    def __str__(self):
        return self.user.username
