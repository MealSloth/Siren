from _include.Chimera.Chimera.models import ContactEmail
from django.forms import *


class ContactEmailForm(Form):
    email = EmailField(max_length=254, required=True, widget=TextInput(attrs={'placeholder': 'Email Address'}))

    def process(self):
        email = self.cleaned_data['email']

        contact_email = ContactEmail(email=email)

        contact_email.save()

        return ContactEmail.objects.filter(email=email).values()[0].get('id')
