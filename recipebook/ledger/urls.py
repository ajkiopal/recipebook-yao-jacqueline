from django.urls import path
from .views import recipe_list, recipe_details

urlpatterns = [
    path("recipes/list/", recipe_list, name="recipe_list"),
    path("recipe/<int:recipe_index>/", recipe_details, name="recipe_details"),
]