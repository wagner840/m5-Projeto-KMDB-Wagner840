from rest_framework import generics, serializers
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsCriticOrReadOnly, IsOwnerOrReadOnly, IsSelfOrAdminReview
from .models import Review
from .serializers import ReviewSerializer
from movies.models import Movie
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied


class ReviewView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCriticOrReadOnly]

    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return Review.objects.filter(movie_id=movie_id)

    def perform_create(self, serializer):
        movie_id = self.kwargs['movie_id']
        movie = get_object_or_404(Movie, pk=movie_id)
        user = self.request.user
        if user.is_superuser:
            raise serializers.ValidationError("Administrators cannot create reviews.")
        if Review.objects.filter(user=user, movie=movie).exists():
            raise serializers.ValidationError("You have already reviewed this movie.")
        serializer.save(user=user, movie=movie)


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

    def get_object(self):
        movie_id = self.kwargs['movie_id']
        review_id = self.kwargs['pk']
        obj = get_object_or_404(Review, movie_id=movie_id, pk=review_id)
        self.check_object_permissions(self.request, obj)
        return obj


class UserReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSelfOrAdminReview]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        if self.request.user.id != user_id and self.request.user.is_superuser:
            raise PermissionDenied("You do not have permission to access another user's reviews.")
        return Review.objects.filter(user_id=user_id)
