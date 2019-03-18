from django.shortcuts import render
from django.http import HttpResponse
# import InstagramAPI
from InstagramAPI.InstagramAPI import InstagramAPI
from django.http import JsonResponse


def index(request):
    api = InstagramAPI("jayabal.al", "jayabal9890@insta")
    if(api.login()):
        api.getSelfUserFeed()
        return JsonResponse(api.LastJson)

    return JsonResponse({})
    # return HttpResponse("Hello, world. You're at the polls index.")
