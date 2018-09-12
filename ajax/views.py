from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User , Group
from django.core import serializers
from django.forms import model_to_dict
from django.shortcuts import render
from django.http import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from account.models import Profile
from ajax.forms import ImageForm
from api.models import Movies, Cast, Movies, Images, Videos, Sequals, Movies, Series, Seasons, Episodes, People, Actors, \
    Cast, CrewPositions, Crew, Barners, Previews
from api.serializers import MoviesSerializer, loginSerializer, GroupSerializer
from rest_framework.authtoken.models import Token
from django_countries import countries
from api.serializers import MoviesSerializer, loginSerializer, UserSerializer

import json
from django.http import JsonResponse


def getcountries(request):
    ctrys = []
    for country in list(countries):
        ctrys.append(country)
    return JsonResponse(ctrys, safe=False)

def getgroups(request):

    print('\n\n\n\n\n\n')
    print(request.POST.get('query'))
    print('\n\n\n\n\n\n')

    if request.method == 'POST':
        if request.POST.get('query'):
            group = Group.objects.filter(name__startswith=request.POST.get('query'))
        elif request.POST.get('name'):
            group = Group.objects.get(name=request.POST.get('name'))
        else:
            group = Group.objects.all()
        groupSerializer = GroupSerializer(group, many=False)
    else:
        group = Group.objects.all()
        groupSerializer = GroupSerializer(group, many=False)
    return JsonResponse(groupSerializer.data, safe=False)

#ASSETS
@login_required
def setlastseen(request):

    if request.method == 'POST':
        return JsonResponse(request.POST, safe=False)
    else:
        user = request.user
        userSerializer = UserSerializer(user, many=False)
        return JsonResponse(userSerializer.data, safe=False)


def savepath(request):
    if request.method == 'POST':
        user = request.user
        userSerializer = UserSerializer(user, many=False)
        return JsonResponse(userSerializer.data, safe=False)
    else:
        user = request.user
        userSerializer = UserSerializer(user, many=False)
        return JsonResponse(userSerializer.data, safe=False)


def settimezone(request):
    if request.method == 'POST':
        user = request.user
        userSerializer = UserSerializer(user, many=False)
        return JsonResponse(userSerializer.data, safe=False)
    else:
        user = request.user
        userSerializer = UserSerializer(user, many=False)
        return JsonResponse(userSerializer.data, safe=False)


def createadmin(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST.get('email'))
            return JsonResponse({'status': 'false', 'error': {'email':'This email already exists. Please use another email'}},status=500)
        except User.DoesNotExist:
            user = User.objects.create_user(
                username=request.POST.get('email'),
                email=request.POST.get('email'),
                password=request.POST.get('password'))
            user.save()
            try:
                profile = Profile.objects.get(user=user)
            except User.DoesNotExist:
                profile = Profile.objects.create(user=user)
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.save()
            profile.country = request.POST.get('country')
            profile.save()
            group = Group.objects.get(name='admins')
            group.user_set.add(user)
            userSerializer = UserSerializer(user, many=False)

            # serialized_obj = serializers.serialize('json', out)
            return JsonResponse(userSerializer.data, safe=False)
    else:
        return JsonResponse({'status': 'false', 'message': 'Please fill the data required for the user submission'},
                            status=500)


def getadmin(request):
    print(request.method)
    if request.method == 'POST':
        user = User.objects.get(username=request.POST.get('username'))
        userSerializer = UserSerializer(user, many=False)
        return JsonResponse(userSerializer.data, safe=False)
    else:
        users = User.objects.filter(groups__name='admins')
        usersSerializer = UserSerializer(users, many=True)
        return JsonResponse(usersSerializer.data, safe=False)

def getmainuser(request):
    user = request.user
    userSerializer = UserSerializer(user, many=False)
    return JsonResponse(userSerializer.data, safe=False)



def add_admin_photo(request):
    photos = Images.objects.all()
    if request.method == 'POST':


        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(request)

            print(user)
            userSerializer = UserSerializer(user, many=False)
            return JsonResponse(userSerializer.data, safe=False)
        else:
            return JsonResponse({'status':'error uploading file form not valid','errors':form.errors.as_json()})



    else:
        return JsonResponse({'status':'send post request'})

