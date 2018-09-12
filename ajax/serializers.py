from rest_framework import serializers
from api.models import Movies, Cast, Images, Videos, Sequals, Series, Seasons, Episodes, People, Actors, Cast, \
    CrewPositions, Crew, Barners, Previews
from django.contrib.auth.models import User
from django.db import models


class loginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class MoviesSerializer(serializers.Serializer):
    class Meta:
        model = Movies
        fields = ('tittle', 'release_date', 'released', 'description', 'thumbnail', 'video', 'sequal')

    def create(self, validated_data):
        sequal_data = validated_data.pop('sequal')
        video_data = validated_data.pop('video')
        thumbnail_data = validated_data.pop('thumbnail')

        user = User.objects.create(**validated_data)

        Sequals.objects.create(user=user, **sequal_data);
        Videos.objects.create(user=user, **video_data);
        Images.objects.create(user=user, **thumbnail_data);

        return user

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


class countriesSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
