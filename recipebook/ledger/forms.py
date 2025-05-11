from django import forms
from .models import RecipeImage, Recipe, RecipeIngredient

class UploadImage(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description']

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity']