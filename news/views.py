import requests
from django.shortcuts import render, HttpResponse

from django_base.settings import NEWS_API_KEY


def fetch_news(request):
    response = requests.get(
        f"https://newsapi.org/v2/top-headlines?category=technology&apiKey={NEWS_API_KEY}"
    )
    if response.status_code != 200:
        return HttpResponse(f"Code: {response.status_code},  Reason: {response.reason}")
    data = response.json()

    return HttpResponse(data["articles"])
