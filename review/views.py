from django.shortcuts import render
from django.http import HttpResponse


def create_review_view(request):
    return HttpResponse("You're looking at question %s.")


def get_review_view(request, review_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % review_id)


def list_reviews_view(request):
    response = "You're looking at the results of question %s."
    return HttpResponse(response)
