from django.shortcuts import render
from .recommender import get_movie_recommendations  # Import recommendation function

def movies_page(request):
    recommendations = None
    error_message = None

    if request.method == "POST":
        movie_title = request.POST.get("movie_title")  # Get input from the form
        recommendations = get_movie_recommendations(movie_title)

        if not recommendations:
            error_message = "Movie not found. Try another movie."

    return render(request, "movies.html", {"recommendations": recommendations, "error_message": error_message})
