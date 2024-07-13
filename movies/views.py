from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Movies

# Create your views here.

def index(request):
    movies = Movies.objects.order_by('publication_date') #se conoce como orm este enlace a base de datos
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'peliculas': movies}, request))

def movie (request, movie_id):
    movie = Movies.objects.get(pk = movie_id)
    template = loader.get_template('display_movies.html')
    context = {
        'peliculas': movie
    }
    return HttpResponse(template.render(context, request))