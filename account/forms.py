from pprint import pprint

from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q

from api.models import Movies,Cast,Movies,Images,Videos,Sequals,Series,Seasons,Episodes,People,Actors,Cast,CrewPositions,Crew,Barners,Previews

from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )
class UserForm(UserCreationForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name','id':'first-name'}))
    last_name  = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name','id':'last-name'}))
    email      = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'jondoe@gmail.com','id':'email'}))
    password1  = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2  = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_email(self):
        try:
            email_passed = self.cleaned_data.get("email")
            User.objects.get(email=email_passed)
            raise forms.ValidationError(email_passed+" email is already in use")
        except User.DoesNotExist:
            return email_passed
