from rest_framework import serializers
from .models import Director, Movie, Review
from django.db.models import Avg


class ReviewSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    director_name = serializers.CharField(source='director.name', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_average_rating(self, obj):
        average = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        return round(average) if average is not None else 0


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = '__all__'

    def get_movies_count(self, obj):
        return obj.movies.count()