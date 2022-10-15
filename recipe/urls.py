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
    path("<int:recipe_id>/delete/", view=views.delete_recipe_view, name="delete"),
]
