from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Images(models.Model):
    file = models.ImageField(u"initial_picture", blank=True, upload_to='images/')
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'


# Songs
class Songs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=100)

    file = models.FileField(blank=True, upload_to='songs/')


# Artists
class Artists(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artist_thumbnail = models.ForeignKey(Images, on_delete=models.CASCADE)


# Albums
class Albums(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=100, )
    release_date = models.DateTimeField()
    description = models.TextField()
    album_thumbnail = models.ForeignKey(Images, on_delete=models.CASCADE)


# Playlist
class Playlists(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playlist_name = models.CharField(max_length=200)
    songs = models.ForeignKey(Songs, on_delete=models.CASCADE)
    created_date = models.DateTimeField()


# Songs Likes
class Songs_Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Songs, on_delete=models.CASCADE)


# Song Listens/Streams
class Song_Listens(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Songs, on_delete=models.CASCADE)
    listened_to = models.IntegerField()
    time = models.TimeField()


class Genres(models.Model):
    name = models.CharField(max_length=100)


class Song_Genres(models.Model):
    song = models.ForeignKey(Songs, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)


class Artist_Genres(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)


class Album_Genres(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)








    # class People(models.Model):
    #     first_name = models.CharField(max_length = 200)
    #     last_name = models.CharField(max_length = 200)
    #     image = models.ForeignKey(Images, on_delete=models.CASCADE)
    #     date_of_birth = models.DateTimeField()
    #     bio =  models.TextField()

    # class Actors(models.Model):
    #     person = models.ForeignKey(People, on_delete=models.CASCADE)


    # class Cast(models.Model):
    #     FOR_TYPES = (
    #         ('M', 'Movie'),
    #         ('E', 'Episode'),
    #     )
    #     actor = models.ForeignKey(Actors, on_delete=models.CASCADE)
    #     for_type = models.CharField(max_length = 1, choices=FOR_TYPES)
    #     movie = models.ForeignKey(Movies, on_delete=models.CASCADE,null=True)
    #     episode = models.ForeignKey(Episodes, on_delete=models.CASCADE,null=True)
    #     character = models.CharField(max_length=200)

    # class CrewPositions(models.Model):
    #     name = models.CharField(max_length = 200)

    # class Crew(models.Model):
    #     person = models.ForeignKey(People, on_delete=models.CASCADE)
    #     crewPosition = models.ForeignKey(CrewPositions, on_delete=models.CASCADE)

    # class Barners(models.Model):
    #     FOR_TYPES = (
    #         ('M', 'Movie'),
    #         ('S', 'Series'),
    #     )
    #     for_type = models.CharField(max_length = 20,choices=FOR_TYPES)
    #     movie = models.ForeignKey(Movies, on_delete=models.CASCADE,null=True)
    #     series = models.ForeignKey(Series, on_delete=models.CASCADE,null=True)
    #     image = models.ForeignKey(Images, on_delete=models.CASCADE,null=True)

    # class Previews(models.Model):
    #     FOR_TYPES = (
    #         ('Movie', 'Movie'),
    #         ('Episode', 'Episode'),
    #         ('Series', 'Series'),
    #     )
    #     forType = models.CharField(max_length=20,choices=FOR_TYPES)
    #     movie = models.ForeignKey(Movies, on_delete=models.CASCADE,null=True)
    #     episode = models.ForeignKey(Episodes, on_delete=models.CASCADE,null=True)
    #     season = models.ForeignKey(Seasons, on_delete=models.CASCADE,null=True)
    #     series = models.ForeignKey(Series, on_delete=models.CASCADE,null=True)
    #     video = models.ForeignKey(Videos, on_delete=models.CASCADE)


    # class Plans(models.Model):
    #     PLAN_TYPES = (
    #         ('free', 'Free'),
    #         ('starter', 'Starter'),
    #         ('premium', 'Premium'),
    #     )
    #     QUALITY_TYPES = (
    #         ('720p', '720p'),
    #         ('1080p', '1080p'),
    #         ('ULTRA HD', 'ULTRA HD'),
    #     )
    #     DEVICES_TYPES = (
    #         ('Mobile + Internet', 'Mobile + Internet'),
    #         ('TV', 'TV'),
    #         ('ALL', 'All'),
    #     )
    #     DURATION_UNIT = (
    #         ('month', 'Month(s)'),
    #         ('yearly', 'Year(s)'),
    #     )
    #     name = models.CharField(max_length=10,choices=PLAN_TYPES)
    #     devices = models.CharField(max_length = 20, choices=DEVICES_TYPES)
    #     quality = models.CharField(max_length = 10, choices=QUALITY_TYPES)
    #     duration_price = models.IntegerField(default=0)
    #     duration = models.IntegerField(default=1)
    #     duration_unit = models.CharField(max_length=10, choices=DURATION_UNIT,default='month')
    #     movies_limit = models.IntegerField(null=True)
    #     shows_limit = models.IntegerField(null=True)
    #     download = models.BooleanField()

    # class Genres(models.Model):
    #     name = models.CharField(max_length=10)
    #     crewPosition = models.ForeignKey(CrewPositions, on_delete=models.CASCADE)

    # # hii ni ya kitu flan
    # class MovieGenres(models.Model):
    #     movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    #     genre = models.ForeignKey(Genres, on_delete=models.CASCADE)

    # class SeriesGenres(models.Model):
    #     series = models.ForeignKey(Series, on_delete=models.CASCADE)
    #     genre = models.ForeignKey(Genres, on_delete=models.CASCADE)