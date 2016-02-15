from _include.Chimera.Chimera.models import Author, Blob
from django import template


register = template.Library()


@register.simple_tag
def author_for_blog_post(blog_post):
    author = Author.objects.filter(id=blog_post.get('author_id')).values()[0]
    return author.get('first_name') + ' ' + author.get('last_name')


@register.simple_tag
def post_time_for_blog_post(blog_post):
    return blog_post.get('post_time')[:11]


@register.simple_tag
def gcs_id_for_blog_post(blog_post):
    return Blob.objects.filter(album_id=blog_post.get('album_id')).values()[0].get('gcs_id')
