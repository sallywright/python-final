from ssl import CertificateError
from urllib import response
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
    all_recipes = []
    for recipe in recipes:
        all_recipes.append(
            {
                "id": recipe.id,
                "title": recipe.title,
                "price": recipe.price,
                "tags": [tag.name for tag in recipe.tags.all()],
            }
        )

    context = {**context, "recipes": all_recipes}
    if request.user.is_authenticated:
        context = {**context, "user_authenticated": True}
        return render(request, "recipes/index.html", context)
    else:
        return render(request, "login/index.html", context)


def delete_recipe_view(request, recipe_id):
    response = "You're looking at the results of %s recipe deletion."
    return HttpResponse(response % recipe_id)


def get_recipe_tags_view(request, recipe_id):
    if request.method == "GET":
        recipe = models.Recipe.objects.filter(id=recipe_id).first()
        already_added_tags = []
        for tag in recipe.tags.all():
            already_added_tags.append(tag.id)

        tags = models.Tag.objects.all().exclude(id__in=already_added_tags)
        context = {"tags": tags, "recipe_id": recipe_id}
        return render(request, "recipes/tags.html", context)


def add_recipe_tag_view(request, recipe_id, tag_id):
    if request.method == "POST":
        recipe = models.Recipe.objects.filter(id=recipe_id).first()
        tag = models.Tag.objects.filter(id=tag_id).first()
        recipe.tags.add(tag)
    return redirect("recipe:list")
