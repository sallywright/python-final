from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("create/", view=views.create_review_view, name="create"),
    path("list/", view=views.list_reviews_view, name="list"),
    path("<int:review_id>/", view=views.get_review_view, name="view"),
]
