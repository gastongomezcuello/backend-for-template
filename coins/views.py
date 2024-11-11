from django.shortcuts import render, redirect


def wallets_view(request):
    return render(request, "coins/wallets.html")


def portfolio_view(request):
    return render(request, "coins/portfolio.html")


def details_view(request):
    return render(request, "coins/details.html")
