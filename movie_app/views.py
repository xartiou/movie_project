from django.shortcuts import render, get_object_or_404
from  .models import Movie
# Create your views here.

def show_all_movies(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movie_app/all_movies.html', context=context)

def show_one_movie(request, id_movie):
    movie = get_object_or_404(Movie, id=id_movie)
    context = {
        'movie': movie
    }
    return render(request, 'movie_app/one_movie.html', context=context)
