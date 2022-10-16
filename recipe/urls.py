from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "recipe"


urlpatterns = [
    path("create/", view=views.create_recipe_view, name="create"),
    path("list/", view=views.list_recipes_view, name="list"),
    path("<int:recipe_id>/", view=views.get_recipe_view, name="view"),
    path(
        "<int:recipe_id>/tags/",
        view=views.get_recipe_tags_view,
        name="view_tags",
    ),
    path(
        "<int:recipe_id>/tags/<int:tag_id>",
        view=views.add_recipe_tag_view,
        name="add_tags",
    ),
    path(
        "<int:recipe_id>/ingredients/",
        view=views.get_recipe_ingredients_view,
        name="view_ingredients",
    ),
    path(
        "<int:recipe_id>/ingredients/<int:ingredient_id>",
        view=views.add_recipe_ingredient_view,
        name="add_ingredient",
    ),
    path(
        "<int:recipe_id>/reviews/create/",
        view=views.add_recipe_review_view,
        name="add_review",
    ),
    path("<int:recipe_id>/delete/", view=views.delete_recipe_view, name="delete"),
]
