from _include.Chimera.Chimera.models import Contact
from datetime import datetime
from django.forms import *


class ContactForm(Form):
    first_name = CharField(max_length=30, required=True, widget=TextInput(attrs={'placeholder': 'First name'}))
    last_name = CharField(max_length=30, required=True, widget=TextInput(attrs={'placeholder': 'Last name'}))
    email = EmailField(max_length=254, required=True, widget=TextInput(attrs={'placeholder': 'Email address'}))
    message = CharField(max_length=1000, required=False, widget=Textarea(attrs={
        'placeholder': 'Message',
        'rows': 5,
    }))

    def process(self):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        time = datetime.utcnow()

        contact = Contact(
            first_name=first_name,
            last_name=last_name,
            email=email,
            message=message,
            time=time,
        )

        contact.save()

        return Contact.objects.filter(email=email).values()[0].get('id')
