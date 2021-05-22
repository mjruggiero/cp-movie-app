from django.shortcuts import render, redirect
from .models import Movie
from django.contrib import messages


def home_page(request):
    user_query = str(request.GET.get('query', ''))
    search_result = Movie.objects.filter(name__icontains=user_query)
    stuff_for_frontend = {"search_result": search_result}
    return render(request, 'movies/movies_stuff.html', stuff_for_frontend)


def create(request):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'picture': request.POST.get('picture'),
            'rating': int(request.POST.get('rating')),
            'notes': request.POST.get('notes'),
        }
        try:
            response = Movie.objects.create(
                name=data.get('name'),
                picture=data.get('picture'),
                rating=data.get('rating'),
                notes=data.get('notes'),
            )
            messages.success(request, f"New movie added: {data.get('name')}")
        except Exception as e:
            messages.warning(
                request, f"Got an error when trying to create new movie: {e}")

    return redirect('/')


def edit(request, movie_id):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'picture': request.POST.get('picture'),
            'rating': int(request.POST.get('rating')),
            'notes': request.POST.get('notes'),
        }
        try:
            movie = Movie.objects.get(id=movie_id)
            movie.name = data.get('name')
            movie.picture = data.get('picture')
            movie.rating = data.get('rating')
            movie.notes = data.get('notes')
            movie.save()
            messages.success(request, f"Movie updated: {data.get('name')}")
        except Exception as e:
            messages.warning(
                request, f"Got an error when trying to update movie: {e}")

    return redirect('/')


def delete(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
        movie_name = movie.name
        movie.delete()
        messages.success(request, f"Movie deleted: {movie_name}")
    except Exception as e:
        messages.warning(
            request, f"Got an error when trying to delete movie: {e}")

    return redirect('/')
