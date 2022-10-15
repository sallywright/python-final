from ssl import CertificateError
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse
from core import models
from django.views.decorators.http import require_http_methods
from datetime import datetime, date


@require_http_methods(["GET", "POST"])
def create_recipe_view(request):
    context = {"user_authenticated": False}
    if request.method == "GET":
        if request.user.is_authenticated:
            context = {**context, "user_authenticated": True}
            return render(request, "recipes/create.html", context)
        else:
            return render(request, "login/index.html", context)
    if request.method == "POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        description = request.POST.get("description")
        created_at = date.today()
        recipe = models.Recipe()
        recipe.title = title
        recipe.price = price
        recipe.description = description
        recipe.created_at = created_at
        try:
            recipe.full_clean()
            recipe.save()
            return redirect("recipe:list")

        except:
            return Http404()


@require_http_methods(["GET"])
def get_recipe_view(request, recipe_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % recipe_id)


@require_http_methods(["GET"])
def list_recipes_view(request):
    context = {"user_authenticated": False}
    recipes = models.Recipe.objects.all()
    context = {**context, "recipes": recipes}
    if request.user.is_authenticated:
        context = {**context, "user_authenticated": True}
        return render(request, "recipes/index.html", context)
    else:
        return render(request, "login/index.html", context)
