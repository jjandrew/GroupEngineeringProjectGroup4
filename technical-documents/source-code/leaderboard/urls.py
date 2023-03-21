from django.urls import path
from .views import leaderboard

""" Defines and names the url that displays the leaderboard.  """
urlpatterns = [
    # Defines and names the url that displays the leaderboard.
    path('', leaderboard, name='leaderboard'),
]
