from django.db import models
from django.contrib.auth.models import User

from django.core import validators
from django.core.validators import RegexValidator

from datetime import timedelta as td


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


class Coin(models.Model):

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    description = models.TextField()
    image = models.ImageField(upload_to="coins")

    def __str__(self):
        return self.name

    def get_date_last_transaction(self):
        return self.transactions.first().date

    def day_average(self, date):
        result = self.transactions.filter(date=date).aggregate(
            average=models.Avg("price")
        )
        return result.get("average", 0.0)

    def last_day_average(self):
        return round(self.day_average(self.get_date_last_transaction()), 2)

    def last_week_variation(self):
        last_week = self.get_date_last_transaction() - td(days=7)
        last_week_avg = self.day_average(last_week)
        last_day_avg = self.last_day_average()
        return round((last_day_avg - last_week_avg) / last_week_avg * 100, 2)

    def day_transactions(self):

        return self.transactions.filter(date=self.get_date_last_transaction())[:8]

    # def last_five_days_average(self, five_days, data ):
    #     averages = []
    #     for day in five_days:
    #         avg = self.day_average(day)
    #         averages.append({"date": day, "avg": avg})
    #     return averages


class Transaction(models.Model):

    CHOICE = (("BUY", "BUY"), ("SELL", "SELL"))

    coin = models.ForeignKey(
        Coin, on_delete=models.CASCADE, related_name="transactions"
    )
    price = models.FloatField()
    amount = models.FloatField()
    date = models.DateTimeField()
    transaction_type = models.CharField(max_length=4, choices=CHOICE)

    def __str__(self):
        return f"{self.coin.name} - {self.transaction_type}"

    def total(self):
        return self.price * self.amount
