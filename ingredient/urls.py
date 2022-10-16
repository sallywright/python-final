from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "ingredients"

urlpatterns = [
    path("create/", view=views.create_ingredient_view, name="create"),
    path("list/", view=views.list_ingredients_view, name="list"),
]
