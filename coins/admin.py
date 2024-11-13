from django.contrib import admin

from coins.models import Card, Coin, Transaction


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("card_name",)


@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Transaction)
class Transaction(admin.ModelAdmin):
    list_display = ("coin", "transaction_type")
