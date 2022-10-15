from django.shortcuts import render
from django.http import HttpResponse


def create_recipe_view(request):
    return HttpResponse("You're looking at question %s.")


def get_recipe_view(request, recipe_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % recipe_id)


def list_recipes_view(request):
    response = "You're looking at the results of question %s."
    return HttpResponse(response)
