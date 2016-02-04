from django.db.models import *
from uuid import uuid4


class BlogPost(Model):
    class Meta:
        db_table = "blog_posts"


class Author(Model):
    class Meta:
        db_table = "authors"


class Contact(Model):
    id = CharField(primary_key=True, default=uuid4, max_length=36, editable=False)
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    email = EmailField(max_length=254)
    message = CharField(max_length=1000)

    class Meta:
        db_table = 'contact_forms'


class ContactEmail(Model):
    id = CharField(primary_key=True, default=uuid4, max_length=36, editable=False)
    email = EmailField(max_length=254)

    class Meta:
        db_table = "contact_emails"
