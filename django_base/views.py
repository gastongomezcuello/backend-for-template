from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):

    data = request.session.get("data", None)
    print(data)
    return render(request, "index.html", {"data": data})
