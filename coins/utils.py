from datetime import datetime, timedelta as td

from django.utils import timezone

from coins.models import Coin, Transaction

import random


def generate_price():
    return random.uniform(5.5, 5045.0) * random.randint(1, 1000)


def generate_amount():
    return random.uniform(0.0001, 100.0) * random.randint(1, 1000)


def generate_transaction():
    today = timezone.now()
    transactions_list = []
    coins = Coin.objects.all()

    for coin in coins:
        for i in range(20):
            transaction = Transaction(
                coin=coin,
                price=generate_price(),
                amount=generate_amount(),
                date=today - td(days=i),
                transaction_type="BUY",
            )
            transactions_list.append(transaction)

        for i in range(20):
            transaction = Transaction(
                coin=coin,
                price=generate_price(),
                amount=generate_amount(),
                date=today - td(days=i),
                transaction_type="SELL",
            )
            transactions_list.append(transaction)

    Transaction.objects.bulk_create(transactions_list)
