from django.urls import path

from coins.views import (
    details_view,
    portfolio_view,
    wallets_view,
    generate_transactions,
)

urlpatterns = [
    path("wallets/", wallets_view, name="wallets"),
    path("portfolio/", portfolio_view, name="portfolio"),
    path("details/", details_view, name="details"),
    path("generate-transactions/", generate_transactions, name="generate_transactions"),
]
