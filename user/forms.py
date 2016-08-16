from django.forms import ModelForm

from .models import User


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['name',
                  'email',
                  'phone',
                  'address',
                  'address2',
                  'city',
                  'state',
                  'zip']

    def clean_zip(self):
        zip_code = self.cleaned_data['zip']
        return str(zip_code)
