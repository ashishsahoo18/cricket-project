from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('player/<int:id>/', views.player_detail, name='player_detail'),
    path("search/", views.live_search, name="live_search"),
]