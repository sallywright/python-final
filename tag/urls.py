from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "tags"

urlpatterns = [
    path("create/", view=views.create_tag_view, name="create"),
    path("list/", view=views.list_tags_view, name="list"),
]
