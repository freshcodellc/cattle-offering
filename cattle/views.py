from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic import View

from .forms import ImportCattleForm
from .models import Cattle


class CattleListView(ListView):
    model = Cattle
    template_name = 'cattle/offering.html'


class CattleDetailView(DetailView):
    model = Cattle
    template_name = 'cattle/offering_detail.html'


class ImportCattleView(View):
    template_name = 'cattle/import-cattle.html'
    success_url = 'success'

    def get(self, request, *args, **kwargs):
        import_form = ImportCattleForm()
        return render(request, self.template_name, {'form': import_form})

    def post(self, request, *args, **kwargs):
        import_form = ImportCattleForm(request.POST, request.FILES)
        if import_form.is_valid():
            valid, form_with_error = import_form.import_cattle()
            if valid:
                return HttpResponseRedirect(self.success_url)
            return render(request, self.template_name, {'form_with_error': form_with_error,
                                                        'form': import_form})
        return render(request, self.template_name, {'form': import_form})
