from django.shortcuts import render
from django.http import HttpResponse


def create_tag_view(request):
    return HttpResponse("You're looking at question %s.")


def get_tag_view(request, tag_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % tag_id)


def list_tags_view(request):
    response = "You're looking at the results of question %s."
    return HttpResponse(response)
