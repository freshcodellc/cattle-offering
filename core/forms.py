from django import forms
from django.template.loader import render_to_string
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'contact-form__name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'contact-form__email'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'contact-form__subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'contact-form__message'}))

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        from_email = 'contact@cattleoffering.com'
        context = {'name': name, 'email': email,'subject': subject, 'message': message}

        text_message = render_to_string('emails/contact.txt', context)
        html_message = render_to_string('emails/contact.html', context)

        if subject and message and email:
            try:
                send_mail(subject, text_message, from_email, ['cody.montgomery@gmail.com'], False,
                          None, None, None, html_message)
            except:
                return False
        else:
            return False
