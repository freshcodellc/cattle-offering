from django.conf import settings
import mailchimp

def get_mailchimp_api():
    return mailchimp.Mailchimp(settings.MAILCHIMP_API_KEY)
