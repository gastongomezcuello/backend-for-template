from datetime import datetime, timedelta as td

from django.utils import timezone

from coins.models import Coin, Transaction

import random


def generate_price():
    return random.uniform(5.5, 5045.0) * random.randint(1, 100)


def generate_amount():
    return random.uniform(0.0001, 100.0) * random.randint(1, 10)


def generate_transaction():
    today = timezone.now()
    transactions_list = []
    coins = Coin.objects.all()

    for coin in coins:
        for i in range(20):
            for j in range(5):
                transaction = Transaction(
                    coin=coin,
                    price=generate_price(),
                    amount=generate_amount(),
                    date=today - td(days=i),
                    transaction_type="BUY",
                )
                transactions_list.append(transaction)

        for i in range(20):
            for j in range(5):
                transaction = Transaction(
                    coin=coin,
                    price=generate_price(),
                    amount=generate_amount(),
                    date=today - td(days=i),
                    transaction_type="SELL",
                )
                transactions_list.append(transaction)

    Transaction.objects.bulk_create(transactions_list)


def get_five_days_average():
    coins = Coin.objects.all()
    transactions = Transaction.objects.all()
    last_date = transactions.first().date
    five_days = [last_date - td(days=i) for i in range(5)]
    data = {"dates": [day.strftime("%d/%m") for day in five_days], "data": []}
    for coin in coins:
        data["data"].append(
            {
                "name": coin.name,
                "data": [coin.day_average(day) for day in five_days],
            }
        )
    return data
