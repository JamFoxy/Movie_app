from rest_framework import serializers
from .models import Director, Movie, Review, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

    def get_movies_count(self, director):
        return director.movie_set.count()


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ['id', 'name', 'movies_count']

    def get_movies_count(self, director):
        return director.movie_set.count()


class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title director genre reviews count_reviews all_reviews average_rating'.split()

    def get_genre(self, movie):
        try:
            return movie.genre.name
        except:
            return 'No genre'

    def get_reviews(self, movie):
        serializer = ReviewSerializer(Review.objects.filter(author__isnull=False, movie=movie), many=True)
        return serializer.data

    def count_reviews(self, reviews):
        return reviews.all().count()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'