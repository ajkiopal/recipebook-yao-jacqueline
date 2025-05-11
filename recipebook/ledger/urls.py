from django.urls import path
from django.contrib.auth import views as auth_views
from .views import recipe_list, recipe_details

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path("recipes/list/", recipe_list, name="recipe_list"),
    path("recipe/<int:recipe_index>/", recipe_details, name="recipe_details"),
]