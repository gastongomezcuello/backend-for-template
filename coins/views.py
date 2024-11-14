from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
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
