from rest_framework import serializers
from movies.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'duration', 'release_date', 'budget', 'synopsis']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.id
        return representation