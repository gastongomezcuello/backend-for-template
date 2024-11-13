import requests
from django.shortcuts import render, HttpResponse
from news.models import News

from django_base.settings import NEWS_API_KEY


def fetch_news(request):
    response = requests.get(
        f"https://newsapi.org/v2/top-headlines?category=technology&apiKey={NEWS_API_KEY}"
    )
    if response.status_code != 200:
        return HttpResponse(f"Code: {response.status_code},  Reason: {response.reason}")
    data = response.json()
    for article in data["articles"]:

        if all(
            article.get(key)
            for key in ["title", "description", "url", "urlToImage", "publishedAt"]
        ):
            News.objects.create(
                title=article["title"],
                description=article["description"],
                url=article["url"],
                url_to_image=article["urlToImage"],
                published_at=article["publishedAt"],
            )

    return HttpResponse("News fetched successfully")
