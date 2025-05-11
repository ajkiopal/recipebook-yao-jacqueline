from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UploadImage, RecipeForm, IngredientForm
from .models import Recipe

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_details', recipe_index=recipe.pk)
    else:
            form = RecipeForm()

    return render(request, 'add_recipe.html', {'form': form})

@login_required
def add_ingredient(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            recipe_ingredient = form.save(commit=False)
            recipe_ingredient.recipe = recipe
            recipe_ingredient.save()
            return redirect('recipe_details', recipe_index=recipe.pk)
    else:
            form = IngredientForm()

    return render(request, 'add_ingredient.html', {'form': form, 'recipe': recipe})

@login_required
def upload_image(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == 'POST':
        form = UploadImage(request.POST, request.FILES)
        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = recipe
            recipe_image.save()
            return redirect('recipe_details', recipe_index=recipe.pk)
    else:
        form = UploadImage()
    return render(request, 'add_image.html', {'form': form, 'recipe': recipe})

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {"recipes": recipes})

@login_required
def recipe_details(request, recipe_index):
    recipe = get_object_or_404(Recipe, id=recipe_index)
    return render(request, "recipe_details.html", {"recipe": recipe})