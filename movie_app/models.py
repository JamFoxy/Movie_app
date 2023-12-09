from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


class Genre(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @property
    def count_movies(self):
        return self.movies.all().count()


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def count_reviews(self):
        reviews = Review.objects.filter(movie=self)
        return reviews.all().count()

    @property
    def average_rating(self):
        return self.reviews.aggregate(Avg('rate_stars'))['rate_stars__avg']

    @property
    def all_reviews(self):
        reviews = Review.objects.filter(movie=self)
        return [{'text': i.text} for i in reviews]


class Review(models.Model):
    STARS = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****'),
    )
    text = models.TextField()
    rate_stars = models.CharField(max_length=100, choices=STARS, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie')

    def __str__(self):
        return self.movie.title


