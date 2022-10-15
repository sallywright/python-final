from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_http_methods
from core import models


@require_http_methods(["GET", "POST"])
def create_tag_view(request):
    context = {"user_authenticated": False}
    if request.method == "GET":
        if request.user.is_authenticated:
            context = {**context, "user_authenticated": True}
            return render(request, "tags/create.html", context)
        else:
            return render(request, "login/index.html", context)
    if request.method == "POST":
        name = request.POST.get("name")
        tag = models.Tag()
        tag.name = name
        tag.user = request.user
        try:
            tag.full_clean()
            tag.save()
            return redirect("recipe:list")

        except:
            return Http404("yet")


def get_tag_view(request, tag_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % tag_id)


def list_tags_view(request):
    response = "You're looking at the results of question %s."
    return HttpResponse(response)
