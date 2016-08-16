from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'contact-form__name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'contact-form__email'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'contact-form__subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'contact-form__message'}))

    def send_email(self):
        # TODO: send email using the self.cleaned_data dictionary
        pass
