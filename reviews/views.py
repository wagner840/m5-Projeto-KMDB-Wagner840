from rest_framework import generics, serializers
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsCriticOrReadOnly
from .models import Review
from .serializers import ReviewSerializer
from movies.models import Movie
from django.shortcuts import get_object_or_404


class ReviewView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCriticOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Review.objects.filter(user=user)

    def perform_create(self, serializer):
        movie_id = self.kwargs["pk"]
        movie = get_object_or_404(Movie, pk=movie_id)
        user = self.request.user
        if user.is_superuser:
            raise serializers.ValidationError("Administrators cannot create reviews.")
        if Review.objects.filter(user=user, movie=movie).exists():
            raise serializers.ValidationError("You have already reviewed this movie.")
        serializer.save(user=user, movie=movie)