from urllib import response
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse
from core import models
from django.views.decorators.http import require_http_methods
from datetime import datetime, date
from django.contrib.auth.decorators import login_required


@login_required
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

        except Exception as e:
            raise Http404(e)


@login_required
@require_http_methods(["GET", "POST"])
def get_recipe_view(request, recipe_id):
    context = {"user_authenticated": False}
    if request.method == "GET":
        if request.user.is_authenticated:
            recipe = models.Recipe.objects.filter(id=recipe_id).first()
            tags = recipe.tags.all()
            ingredients = recipe.ingredients.all()
            reviews = recipe.reviews.all()

            context = {
                **context,
                "user_authenticated": True,
                "recipe": recipe,
                "tags": tags,
                "ingredients": ingredients,
                "reviews": reviews,
            }
            return render(request, "recipes/view.html", context)
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

        except Exception as e:
            raise Http404(e)


@login_required
@require_http_methods(["GET"])
def list_recipes_view(request):
    context = {"user_authenticated": False}
    if request.method == "GET":
        if request.user.is_authenticated:
            context = {**context, "user_authenticated": True}
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


@login_required
def get_recipe_tags_view(request, recipe_id):
    if request.method == "GET":
        context = {"user_authenticated": False}
        if request.user.is_authenticated:
            context = {**context, "user_authenticated": True}
        recipe = models.Recipe.objects.filter(id=recipe_id).first()
        already_added_tags = []
        for tag in recipe.tags.all():
            already_added_tags.append(tag.id)

        tags = models.Tag.objects.all().exclude(id__in=already_added_tags)
        context = {**context, "tags": tags, "recipe_id": recipe_id}
        return render(request, "recipes/tags.html", context)


@login_required
def add_recipe_tag_view(request, recipe_id, tag_id):
    if request.method == "POST":
        recipe = models.Recipe.objects.filter(id=recipe_id).first()
        tag = models.Tag.objects.filter(id=tag_id).first()
        recipe.tags.add(tag)
    return redirect("recipe:list")


@login_required
def get_recipe_ingredients_view(request, recipe_id):
    if request.method == "GET":
        context = {"user_authenticated": False}
        if request.user.is_authenticated:
            context = {**context, "user_authenticated": True}
        recipe = models.Recipe.objects.filter(id=recipe_id).first()
        already_added_ingredients = []
        for ingredient in recipe.ingredients.all():
            already_added_ingredients.append(ingredient.id)

        ingredients = models.Ingredient.objects.all().exclude(
            id__in=already_added_ingredients
        )
        context = {**context, "ingredients": ingredients, "recipe_id": recipe_id}

        return render(request, "recipes/ingredients.html", context)


@login_required
def add_recipe_ingredient_view(request, recipe_id, ingredient_id):
    if request.method == "POST":
        recipe = models.Recipe.objects.filter(id=recipe_id).first()
        ingredient = models.Ingredient.objects.filter(id=ingredient_id).first()
        recipe.ingredients.add(ingredient)
    return redirect("recipe:view", recipe_id)


@login_required
def add_recipe_review_view(request, recipe_id):

    if request.method == "POST":
        title = request.POST.get("title")
        comment = request.POST.get("comment")
        created_at = datetime.now()
        recipe = models.Recipe.objects.filter(id=recipe_id).first()
        review = models.Review()
        review.title = title
        review.comment = comment
        review.created_at = created_at
        review.user = request.user

        try:
            review.full_clean()
            review.save()
            recipe.reviews.add(review)
            return redirect("recipe:view", recipe_id)

        except Exception as e:
            raise Http404(e)

    context = {"user_authenticated": False}
    if request.method == "GET":
        if request.user.is_authenticated:
            context = {**context, "user_authenticated": True, "recipe_id": recipe_id}
            return render(request, "recipes/reviews.html", context)
        else:
            return render(request, "login/index.html", context)
