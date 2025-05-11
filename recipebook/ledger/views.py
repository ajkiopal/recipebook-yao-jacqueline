from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {"recipes": recipes})

@login_required
def recipe_details(request, recipe_index):
    recipe = get_object_or_404(Recipe, id=recipe_index)
    return render(request, "recipe_details.html", {"recipe": recipe})