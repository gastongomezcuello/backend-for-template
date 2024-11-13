from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

from coins.utils import generate_transaction

from coins.models import Coin, Transaction

from datetime import timedelta as td


@login_required
def wallets_view(request):
    return render(request, "coins/wallets.html")


@login_required
def portfolio_view(request):
    return render(request, "coins/portfolio.html")


@login_required
def details_view(request):
    return render(request, "coins/details.html")


def generate_transactions(request):
    generate_transaction()
    return HttpResponse("Transactions generated")


def get_five_days_average(request):
    coins = Coin.objects.all()
    transactions = Transaction.objects.all()
    last_date = transactions.first().date
    five_days = [(last_date - td(days=i)).strftime("%d/%m") for i in range(5)]
    data = {"dates": five_days, "data": []}
    for coin in coins:
        data["data"].append(
            {
                "name": coin.name,
                "data": [coin.day_average(day) for day in five_days],
            }
        )
    return HttpResponse(data)


{
    "dates": ["26/02", "25/02", "24/02", "23/02", "22/02"],
    "data": [
        {
            "name": "Bitcoin",
            "data": [14406.322580645161, 14776.016129032258, 17000, 13000, 25000],
        },
        {"name": "Ethereum", "data": [2500, 2520, 2530, 4000, 16000]},
        {"name": "Monero", "data": [1230, 1180, 1310, 1450, 2350]},
        {"name": "Litecoin", "data": [345, 367, 387, 415, 420]},
    ],
}
