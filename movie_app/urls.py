from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/directors/', views.get_all_director_list),
    path('api/v1/directors/<int:director_id>/', views.director_details),
    path('api/v1/movies/', views.get_all_movie_list),
    path('api/v1/movies/<int:movie_id>/', views.movie_details),
    path('api/v1/reviews/', views.get_all_review_list),
    path('api/v1/reviews/<int:review_id>/', views.review_details),
]