from django.urls import path
from .views import *

urlpatterns = [
    path("recipes/list/", recipe_list, name="recipe_list"),
    path("recipe/<int:recipe_index>/", recipe_details, name="recipe_details"),
]