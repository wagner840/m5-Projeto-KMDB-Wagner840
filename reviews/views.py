from rest_framework import generics
from reviews.models import Review
from reviews.serializers import ReviewSerializer

class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer