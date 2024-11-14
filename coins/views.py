from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from coins.utils import generate_transaction
from coins.forms import CardForm
from coins.models import Coin, Transaction, Card

from datetime import datetime, timedelta as td


@login_required
def wallets_view(request):
    if request.method == "GET":
        context = {
            "cards": Card.objects.all(),
        }
        return render(request, "coins/wallets.html", context=context)
    elif request.method == "POST":

        data = request.POST.copy()
        data["valid_date"] = datetime.strptime(data["valid_date"], "%m/%y")

        form = CardForm(data=data)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = request.user
            card.save()
            return redirect("wallets")
        else:
            errors = form.errors
            context = {
                "errors": errors,
            }
            return render(request, "coins/wallets.html", context=context)


def delete_card(request, card_id):
    Card.objects.get(id=card_id).delete()
    return redirect("wallets")


@login_required
def portfolio_view(request):
    return render(request, "coins/portfolio.html")


@login_required
def details_view(request):
    return render(request, "coins/details.html")


def generate_transactions(request):
    generate_transaction()
    return HttpResponse("Transactions generated")
