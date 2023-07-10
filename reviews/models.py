from django.db import models
from movies.models import Movie
from users.models import User


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=0)
    review_text = models.TextField( max_length=1000)
    spoiler = models.BooleanField(default=False)