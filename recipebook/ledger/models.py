from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="")
    bio = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    name = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name
    

class Recipe(models.Model):
    name = models.CharField(max_length=255, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    CreatedOn = models.DateField(auto_now_add=True)
    UpdatedOn = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:getRecipe', args=[self.pk])
    

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredient")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_ingredients")

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name}"