from django.views.generic import ListView
from django.shortcuts import render

from .models import Cattle

class CattleListView(ListView):
    model = Cattle
    template_name = 'cattle/offering.html'
