from django.urls import path
from .views import movies_page

urlpatterns = [
    path("", movies_page, name="movies_page"),
]

