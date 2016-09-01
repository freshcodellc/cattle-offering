from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
from django.core.urlresolvers import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

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
        return super(RegistrationView, self).form_valid(form)


class EditProfileView(UpdateView):
    model = get_user_model()
    fields = ['name',
              'email',
              'phone',
              'address',
              'address2',
              'city',
              'state',
              'zip',
              'newsletter']
    template_name = 'user/profile-edit.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'Profile saved successfully.')
        return reverse('edit-profile', args=(self.kwargs['pk'],))


class WatchListView(ListView):
    model = Cattle
    template_name = 'user/watch_list.html'

    def get_queryset(self):
        return self.request.user.watch_list.all()
