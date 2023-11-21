from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from rest_framework import status

@api_view(['GET'])
def get_all_director_list(request):
    directors = Director.objects.all()
    data = DirectorSerializer(directors, many=True).data
    return Response(data)

@api_view(['GET'])
def director_details(request, director_id):
    try:
        director = Director.objects.get(id=director_id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': "Режиссер не найден"})
    data = DirectorSerializer(director).data
    return Response(data=data)

@api_view(['GET'])
def get_all_movie_list(request):
    movies = Movie.objects.all()
    data = MovieSerializer(movies, many=True).data
    return Response(data)


@api_view(['GET'])
def movie_details(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': "Фильм не найден"})
    data = MovieSerializer(movie).data
    return Response(data=data)


@api_view(['GET'])
def get_all_review_list(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(reviews, many=True).data
    return Response(data)

# Вывести один отзыв
@api_view(['GET'])
def review_details(request, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': "Отзыв не найден"})
    data = ReviewSerializer(review).data
    return Response(data=data)