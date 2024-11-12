from django.db import models
from django.contrib.auth.models import User

from django.core import validators
from django.core.validators import RegexValidator


class Card(models.Model):

    CHOICES = (
        ("#FF5733", "Orange"),
        ("#33FFFC", "Blue"),
        ("#DAF7A6", "Green"),
        ("#581845", "Purple"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cards")
    card_name = models.CharField(max_length=255)
    card_holder = models.CharField(max_length=255)
    card_number = models.CharField(
        max_length=16, validators=[RegexValidator(r"^[0-9]{16}$")]
    )
    bank_name = models.CharField(max_length=255)
    valid_date = models.DateField()
    color = models.CharField(max_length=7, choices=CHOICES, default="#FF5733")

    def __str__(self):
        return self.card_name
