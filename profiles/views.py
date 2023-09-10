from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .forms import ProfileForm
from .models import UserProfile


class CreateProfileView(CreateView):
    model = UserProfile
    fields = '__all__'
    template_name = 'profiles/create_profile.html'
    success_url = '/profiles'


class UserProfilesView(ListView):
    template_name = 'profiles/user_profiles.html'
    model = UserProfile
    context_object_name = 'profiles'
