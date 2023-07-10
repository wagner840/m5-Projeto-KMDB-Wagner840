from django.urls import path
from . import views

urlpatterns = [
    path("movies/", views.MovieListCreate.as_view()),
    path("movies/<int:pk>/", views.MovieDetailView.as_view()),
]