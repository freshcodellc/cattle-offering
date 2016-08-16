from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Cattle

class CattleListView(ListView):
    model = Cattle
    template_name = 'cattle/offering.html'

class CattleDetailView(DetailView):
    model = Cattle
    template_name = 'cattle/offering_detail.html'
