from django.urls import path
from .views import directors_list_view, directors_detail_view, movies_list_view, movies_detail_view, movies_reviews_view ,reviews_list_view, reviews_detail_view

urlpatterns = [
    path('directors/', directors_list_view, name='directors_list'),
    path('directors/<int:id>/', directors_detail_view, name='directors_detail'),

    path('movies/', movies_list_view, name='movies_list'),
    path('movies/<int:id>/', movies_detail_view, name='movies_detail'),

    path('movies/reviews/', movies_reviews_view, name='movies_reviews'),
    path('reviews/', reviews_list_view, name='reviews_list'),
    path('reviews/<int:id>/', reviews_detail_view, name='reviews_detail'),
]