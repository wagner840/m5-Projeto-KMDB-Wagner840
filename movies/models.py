from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=127, unique=True)
    duration = models.CharField(max_length=15)
    release_date = models.PositiveSmallIntegerField()
    budget = models.IntegerField()
    synopsis = models.TextField(max_length=1000)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('title', 'release_date',)
    
