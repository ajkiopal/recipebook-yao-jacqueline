from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, Profile, RecipeImage
from django.contrib.auth.models import User

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

    list_display = ('name',)

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

    list_display = ('name', 'author', 'CreatedOn', 'UpdatedOn')
    inlines = [RecipeImageInline]

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

    list_display = ('quantity',)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    fields = ['author_name', 'bio']

class CustomUserAdmin(UserAdmin):
    inline = [ProfileInline]

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(RecipeImage)