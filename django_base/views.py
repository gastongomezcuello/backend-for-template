from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from coins.models import Coin, Transaction
from coins.utils import get_five_days_average


@login_required
def index(request):

    data = get_five_days_average()
    context = {
        "data": data,
        "coins": Coin.objects.all(),
    }

    return render(request, "index.html", context=context)
