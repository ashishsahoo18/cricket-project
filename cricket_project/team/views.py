from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Player


# Home Page
def home(request):

    query = request.GET.get('q')
    country = request.GET.get('country')

    players = Player.objects.all()

    # Search
    if query:
        players = players.filter(name__icontains=query)

    # Country Filter
    if country:
        players = players.filter(country=country)

    return render(request, "team/home.html", {
        "players": players
    })


# Player Detail Page
def player_detail(request, id):

    player = get_object_or_404(Player, id=id)

    return render(request, "team/player_detail.html", {
        "player": player
    })


# Live Search
def live_search(request):

    query = request.GET.get('q')

    players = Player.objects.filter(name__icontains=query)

    data = []

    for player in players:

        data.append({
            "name": player.name,
            "country": player.country,
            "image": player.image.url if player.image else "",
            "id": player.id
        })

    return JsonResponse({
        "players": data
    })