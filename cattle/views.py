from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
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

    def dispatch(self, request, *args, **kwargs):
        if not request.user or request.user.is_anonymous():
            messages.add_message(request, messages.INFO, 'You must sign up for an account before you can access full listings.')
            return redirect('/account/register')
        return super(CattleDetailView, self).dispatch(request, *args, **kwargs)


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
