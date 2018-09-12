from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Images, Videos, Sequals, Movies, Series, Seasons, Episodes, People, Actors, Cast, CrewPositions, Crew, Barners, Previews,  Plans
from account.models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


class MoviesAdmins(admin.ModelAdmin):
    list_display = ['tittle', 'release_date', 'released', 'sequal', 'video', 'description', 'thumbnail']


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['file']  # pip install pillow


class VideosAdmin(admin.ModelAdmin):
    list_display = ['thumbnail', 'location']


class SequalsAdmin(admin.ModelAdmin):
    list_display = ['tittle', 'thumbnail']


class SeriesAdmin(admin.ModelAdmin):
    list_display = ['tittle', 'description', 'release_date', 'thumbnail']


class SeasonsAdmin(admin.ModelAdmin):
    list_display = ['tittle', 'series']


class EpisodesAdmin(admin.ModelAdmin):
    list_display = ['tittle', 'season', 'air_datetime', 'video']


class PeopleAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'image', 'date_of_birth', 'bio']


class ActorsAdmin(admin.ModelAdmin):
    list_display = ['person']


class CastAdmin(admin.ModelAdmin):
    list_display = ['actor', 'for_type', 'movie', 'episode', 'character']


class CrewPositionsAdmin(admin.ModelAdmin):
    list_display = ['name']


class CrewAdmin(admin.ModelAdmin):
    list_display = ['person', 'crewPosition']


class BarnersAdmin(admin.ModelAdmin):
    list_display = ['movie', 'series', 'image']


class PreviewsAdmin(admin.ModelAdmin):
    list_display = ['forType', 'movie', 'episode', 'season', 'series', 'video']

class PlansAdmin(admin.ModelAdmin):
    list_display = ['name', 'devices', 'quality', 'movies_limit', 'shows_limit', 'download', 'duration_price', 'duration', 'duration_unit']


admin.site.register(Movies, MoviesAdmins)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Videos, VideosAdmin)
admin.site.register(Sequals, SequalsAdmin)

admin.site.register(Series, SeriesAdmin)
admin.site.register(Seasons, SeasonsAdmin)
admin.site.register(Episodes, EpisodesAdmin)
admin.site.register(People, PeopleAdmin)
admin.site.register(Actors, ActorsAdmin)
admin.site.register(Cast, CastAdmin)
admin.site.register(CrewPositions, CrewPositionsAdmin)
admin.site.register(Crew, CrewAdmin)
admin.site.register(Barners, BarnersAdmin)
admin.site.register(Previews, PreviewsAdmin)
admin.site.register(Plans, PlansAdmin)
