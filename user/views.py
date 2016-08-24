from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import User
from cattle.models import Cattle


class RegistrationView(CreateView):
    model = get_user_model()
    fields = ['name', 'email', 'password', 'newsletter']
    template_name = 'registration/signup.html'
    success_url = '/thanks/'

    def form_valid(self, form):
        user = form.save(False)
        user.type = user.BUYER
        user.set_password(user.password)
        user.save()
        if user.newsletter:
            user.add_email_to_mailing_list()
        user = authenticate(username=user.email, password=form.cleaned_data['password'])
        login(self.request, user)
        return super().form_valid(form)


class WatchListView(ListView):
    model = Cattle
    template_name = 'user/watch_list.html'

    def get_queryset(self):
        return self.request.user.watch_list.all()
