from django.shortcuts import render
from django.http import HttpResponse


def create_ingredient_view(request):
    return HttpResponse("You're looking at question %s.")


def get_ingredient_view(request, ingredient_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % ingredient_id)


def list_ingredients_view(request):
    response = "You're looking at the results of question %s."
    return HttpResponse(response)
