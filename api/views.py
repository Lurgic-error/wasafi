from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import  Movies,Cast,Movies,Images,Videos,Sequals,Movies,Series,Seasons,Episodes,People,Actors,Cast,CrewPositions,Crew,Barners,Previews
from api.serializers import  MoviesSerializer, loginSerializer
from rest_framework.authtoken.models import Token

class login(APIView):
    def post(self,request, format=None):

        print(request.data)
        serializer = loginSerializer(data = request.data)


        if serializer.is_valid():

            username = serializer.data['username']
            password = serializer.data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'user_id': user.pk,
                    'email': user.email
                })
                return Response(Response, status=status.HTTP_201_CREATED)
            else:
                content = {'status': 'user not found'}
                return Response(content, status=status.HTTP_401_UNAUTHORIZED)
        else:
           content = {'status': 'please provide username and password'}
           return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

class movieList(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    def get_object(self, pk):
        try:
            return Movies.objects.get(pk=pk)
        except Movies.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        movies = Movies.objects.all();
        serializer = MoviesSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MoviesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
