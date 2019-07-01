from django.urls import path
from .views import ListAllMovies, AddMovie, MoviesByUser


urlpatterns = [
    path('movies/', ListAllMovies.as_view()),
    path('add/', AddMovie.as_view()),
    path('users_movies/', MoviesByUser.as_view()),
]