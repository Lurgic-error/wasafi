from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.urls import reverse
from api.models import Movies, Cast, Movies, Images, Videos, Sequals, Series, Seasons, Episodes, People, Actors, Cast, CrewPositions, Crew, Barners, Previews, Plans
from django.contrib.auth.models import User
from .forms import UserForm

def signup(request, section, vars = None):
    section = int(section)
    if section == 1:
        if not request.user.is_authenticated:
            plans = Plans.objects.all();
            for e in plans:
                print(e)
            return render(request, 'auth/signup-step1.html', {
                'section' : section,
                'plans': plans,
                'request': request,
            })
        else:
            return redirect(index)
    elif section == 2:
        if not request.user.is_authenticated:
            if request.method == 'POST':

                request.session['plan'] = vars
                request.POST = request.POST.copy()
                request.POST['username'] = request.POST['email']
                form = UserForm(request.POST)

                if form.is_valid():

                    user = form.save()
                    user = User.objects.get(username=user)
                    user.refresh_from_db()  # load the profile instance created by the signal
                    #user.profile.birth_date = form.cleaned_data.get('birth_date')
                    #user.save()

                    username = form.cleaned_data.get('username')
                    raw_password = form.cleaned_data.get('password1')
                    user = authenticate(request, username=username, password=raw_password)
                    login(request, user)
                    return redirect(signup, section=3, vars=0)
            else:
                form = UserForm()

            return render(request, 'auth/signup-step2.html', {
                'section': section,
                'form': form,
                'request': request,
            })
        else:
            return redirect(index)
    elif section == 3:
        if request.user.is_authenticated:
            return render(request, 'auth/signup-step3.html', {
                'section': section,
                'barners': False,
            })
        else:
            return redirect(signup,section=1,vars=0)
    elif section == 4:
        if request.user.is_authenticated:
            return render(request, 'auth/signup-step4.html', {
                'section' : section,
                'request': request,
            })
        else:
            return redirect(signup,section=1,vars=0)

    elif section == 5:
        if request.user.is_authenticated:
            return render(request, 'auth/signup-step4.html', {
                'section' : section,
                'request': request,
            })
        else:
            return redirect(signup, section=1, vars=0)
    else:
        raise Http404('page doesnt exist')

def auth_login(request):

    form = UserForm(request.POST)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(request, username=username, password=raw_password)
        if user is not None:
            return_url = '';
            # A backend authenticated the credentials
        else:
            return_url = '';
            # No backend authenticated the credentials
    else:
        form = UserForm()

def seetings(request):
    q = 1;