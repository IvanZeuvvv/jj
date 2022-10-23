from .models import Advertisement
from django.views import generic, View
from django.shortcuts import render
from django.http import HttpResponseRedirect


class AdvertisementListView(generic.ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    context_object_name = 'advertisement_list'


class AdvertisementDetailView(generic.DetailView):
    model = Advertisement
    template_name = 'advertisement/advertisement-detail.html'
    context_object_name = 'detail_list'