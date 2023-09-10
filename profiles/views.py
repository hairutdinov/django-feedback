from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from .forms import ProfileForm
from .models import UserProfile


class CreateProfileView(CreateView):
    model = UserProfile
    fields = '__all__'
    template_name = 'profiles/create_profile.html'
    success_url = '/profiles'
