from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from core import models
from django.http import HttpResponse, Http404


@require_http_methods(["GET", "POST"])
def create_ingredient_view(request):
    context = {"user_authenticated": False}
    if request.method == "GET":
        if request.user.is_authenticated:
            context = {**context, "user_authenticated": True}
            return render(request, "ingredients/create.html", context)
        else:
            return render(request, "login/index.html", context)
    if request.method == "POST":
        name = request.POST.get("name")
        ingredient = models.Ingredient()
        ingredient.name = name
        ingredient.user = request.user
        try:
            ingredient.full_clean()
            ingredient.save()
            return redirect("ingredients:list")

        except:
            return Http404("yet")


def get_ingredient_view(request, ingredient_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % ingredient_id)


def list_ingredients_view(request):
    context = {"user_authenticated": False}
    if request.method == "GET":
        if request.user.is_authenticated:
            context = {**context, "user_authenticated": True}
        ingredients = models.Ingredient.objects.all()
        context = {**context, "ingredients": ingredients}
        return render(request, "ingredients/index.html", context)
