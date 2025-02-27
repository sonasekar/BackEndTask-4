import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset: Movies with genre and ratings
movies = [
    {"id": 1, "title": "Inception", "genre": "Sci-Fi", "rating": 9.0},
    {"id": 2, "title": "Titanic", "genre": "Romance", "rating": 8.5},
    {"id": 3, "title": "The Matrix", "genre": "Sci-Fi", "rating": 8.7},
    {"id": 4, "title": "Interstellar", "genre": "Sci-Fi", "rating": 9.1},
    {"id": 5, "title": "The Notebook", "genre": "Romance", "rating": 8.0},
]

def get_movie_recommendations(movie_title):
    genres = {m["title"]: m["genre"] for m in movies}
    ratings = {m["title"]: m["rating"] for m in movies}

    if movie_title not in genres:
        return []

    input_genre = genres[movie_title]
    input_rating = ratings[movie_title]

    feature_matrix = np.array([[m["rating"]] for m in movies])
    
    similarity_scores = cosine_similarity(feature_matrix, feature_matrix)

    movie_index = next(i for i, m in enumerate(movies) if m["title"] == movie_title)

    similar_movies = sorted(
        enumerate(similarity_scores[movie_index]), key=lambda x: x[1], reverse=True
    )

    recommended_movies = [
        movies[i]["title"]
        for i, score in similar_movies[1:4]
        if genres[movies[i]["title"]] == input_genre
    ]
    
    return recommended_movies
