from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

from .models import User


class Signup(CreateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'password', 'newsletter']
    template_name = 'registration/signup.html'
    success_url = '/thanks/'

    def form_valid(self, form):
        user = form.save(False)
        user.type = user.BUYER
        user.set_password(user.password)
        user.save()
        user = authenticate(username=user.email, password=form.cleaned_data['password'])
        login(self.request, user)
        return super().form_valid(form)
