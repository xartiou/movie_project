from django.shortcuts import render, get_object_or_404
from  .models import Movie
from django.db.models import F
# функции агрегации
from django.db.models import Sum, Avg, Max, Min, Count

# Create your views here.


def show_all_movies(request):
    movies = Movie.objects.order_by(F('year').desc(nulls_last=True))  # или .asc или nulls_first=True
    agg = movies.aggregate(Avg("budget"), Min("rating"), Max("rating"))
    for movie in movies:
        movie.save()
    context = {
        'movies': movies,
        'agg': agg,
        'count_mov': movies.count()
    }
    return render(request, 'movie_app/all_movies.html', context=context)

def show_one_movie(request, slug_movie:str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    context = {
        'movie': movie
    }
    return render(request, 'movie_app/one_movie.html', context=context)
