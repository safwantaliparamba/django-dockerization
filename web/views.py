from django.shortcuts import render
from django.http.response import HttpResponse


def index(request):
    return HttpResponse("<h1>Dockerization of Django App <h1/>")