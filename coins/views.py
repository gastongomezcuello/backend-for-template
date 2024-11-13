from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def wallets_view(request):
    return render(request, "coins/wallets.html")


@login_required
def portfolio_view(request):
    return render(request, "coins/portfolio.html")


@login_required
def details_view(request):
    return render(request, "coins/details.html")
