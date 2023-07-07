from rest_framework import generics
from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieListCreate(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer