from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms

# Create your views here.
class ChannelCreate(CreateView):
    form_class = forms.ChannelCreateForm
    success_url = reverse_lazy('home') #change it later to my_teams
    template_name = 'channels/create_channel.html'