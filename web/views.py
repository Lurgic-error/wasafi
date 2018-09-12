from pprint import pprint

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404,HttpRequest,HttpResponseRedirect

from django.urls import reverse
from django.views.generic import TemplateView
from api.models import Movies, Cast, Movies, Images, Videos, Sequals, Series, Seasons, Episodes, People, Actors, Cast, CrewPositions, Crew, Barners, Previews, Plans
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth.models import Group, Permission, User

try:
    Group.objects.get(name='admins')
except Group.DoesNotExist:
    new_group, created = Group.objects.get_or_create(name='admins')
    superusers = User.objects.filter(is_superuser=True)
    for superuser in superusers:
        new_group.user_set.add(superuser)

# Code to add permission to group ???
# ct = ContentType.objects.get_for_model(Project)

# Now what - Say I want to add 'Can add project' permission to new_group?
#permission = Permission.objects.create(codename='can_add_project',  name='Can add project', content_type=ct)
#new_group.permissions.add(permission)

def index(request):
    return render(request, 'index.html', {
        'barners': False,
        'request': request,
    })


@login_required
def home(request):
    # my_partials = urls_by_namespace('partials')
    return render(request, 'dashboard/headers_footers/dashboard_block.html', {
        'is_authenticated': request.user.is_authenticated,
    })

# angular js partials
class PartialGroupView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(PartialGroupView, self).get_context_data(**kwargs)
        # update the context
        return context

def live(request):
    return HttpResponse('<p>In live view</p>')
