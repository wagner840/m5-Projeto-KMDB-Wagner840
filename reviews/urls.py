from django.urls import path
from . import views

urlpatterns = [
    path("movies/<int:movie_id>/reviews/", views.ReviewView.as_view()),
    path("movies/<int:movie_id>/reviews/<int:pk>/", views.ReviewDetailView.as_view()),
    path("users/<int:user_id>/reviews/", views.UserReviewListView.as_view()),
]