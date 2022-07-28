from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("this is index page")


def getvideos(request):
    myjson = {
        "name": "arbab halgheha",
        "qulity": "720",
        "size": 1200
    }
    return JsonResponse(myjson)
