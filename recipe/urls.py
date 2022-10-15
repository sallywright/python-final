from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("create/", view=views.create_recipe_view, name="create"),
    path("list/", view=views.list_recipes_view, name="list"),
    path("<int:recipe_id>/", view=views.get_recipe_view, name="view"),
]
