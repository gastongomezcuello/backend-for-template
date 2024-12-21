
from django.shortcuts import render
from coins.models import Coin, Transaction
from coins.utils import get_five_days_average, get_random_recent_transactions



def index(request):

    data = get_five_days_average()
    random_transactions = get_random_recent_transactions()
    context = {
        "data": data,
        "coins": Coin.objects.all(),
        "transactions": random_transactions,
    }

    return render(request, "index.html", context=context)
