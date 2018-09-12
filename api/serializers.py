from django_countries.fields import Country
from rest_framework import serializers
from api.models import Movies, Cast, Images, Videos, Sequals, Series, Seasons, Episodes, People, Actors, Cast, \
    CrewPositions, Crew, Barners, Previews
from django.contrib.auth.models import User, Group
from account.models import Profile
from django.db import models
from django_countries import countries
from django_countries.serializers import CountryFieldMixin

from cloudsplus import settings


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



class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = ('file', 'description', 'uploaded_at')

class ProfileSerializer(CountryFieldMixin,serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    # image = ImagesSerializer(many=False)
    class Meta:
        model = Profile
        fields = ('country', 'image', 'birthdate')
    def get_image(self,obj):
        if not obj.image:
            image = Images.objects.get(pk=1)
            return ImagesSerializer(image, many=False).data
        else:
            # image = Images.objects.get(pk=obj.image)
            return ImagesSerializer(obj.image,many=False).data


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=False)
    full_name = serializers.SerializerMethodField('create_full_name')  # no corresponding model property.

    def create_full_name(self,obj):
        try:
            profile = Profile.objects.get(user=obj)
        except Profile.DoesNotExist:
            profile = Profile.objects.create(user=obj)
        name = (obj.first_name.capitalize()+' '+obj.last_name.capitalize() if obj.first_name != "" else obj.username)
        return name

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'profile','full_name')

class PermissonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class GroupPermissonsSerializer(serializers.ModelSerializer):
    permission = PermissonsSerializer(many=False)
    class Meta:
        model = Group
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    # permissions = serializers.SerializerMethodField()
    class Meta:
        model = Group
        # fields = ('name','permissions')
        fields = '__all__'

    def get_image(self,obj):
            return GroupPermissonsSerializer(obj.permissions.all(), many=True).data
