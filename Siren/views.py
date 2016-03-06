from _include.Chimera.Chimera.settings import GCS_URL, PROTOCOL
from form.contact.form_contact_email import ContactEmailForm
from django.http import HttpResponse, HttpResponseRedirect
from _include.Chimera.Chimera.models import BlogPost
from form.contact.form_contact import ContactForm
from django.core.urlresolvers import reverse
from django.template import Context
from django.shortcuts import render


def home(request):
    warning = ''
    if request.method == 'POST':
        form = ContactEmailForm(request.POST)
        if form.is_valid():
            contact_email_id = form.process()
            url = reverse('thanks', args=['email', contact_email_id])
            return HttpResponseRedirect(url)
        else:
            warning = 'Invalid Email'

    response = render(request, 'page/home.html', Context({'form': ContactEmailForm, 'warning': warning, }))
    return HttpResponse(response)


def about(request):
    warning = ''
    if request.method == 'POST':
        form = ContactEmailForm(request.POST)
        if form.is_valid():
            contact_email_id = form.process()
            url = reverse('thanks', args=['email', contact_email_id])
            return HttpResponseRedirect(url)
        else:
            warning = 'Invalid Email'

    response = render(request, 'page/about.html', Context({'form': ContactEmailForm(), 'warning': warning, }))
    return HttpResponse(response)


def blog(request):
    blog_post_list = list(BlogPost.objects.all().order_by('-post_time').values())
    response = render(request, 'page/blog.html', Context({'blog_post_list': blog_post_list, 'url': PROTOCOL + GCS_URL}))
    return HttpResponse(response)


def blog_post(request, blog_post_id):
    current_blog_post = BlogPost.objects.filter(id=blog_post_id).values()[0]
    blog_post_list = list(BlogPost.objects.order_by('-post_time').all().values())
    response = render(request, 'page/blog-post.html', Context({
        'blog_post': current_blog_post, 'blog_post_list': blog_post_list, 'url': PROTOCOL + GCS_URL,
    }))
    return HttpResponse(response)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_id = form.process()
            url = reverse('thanks', args=['contact', contact_id])
            return HttpResponseRedirect(url)
        else:
            return HttpResponseRedirect('/')

    response = render(request, 'page/contact.html', Context({'form': ContactForm()}))
    return HttpResponse(response)


def thanks(request, thank_type, unique_id):
    response = render(request, 'page/thanks.html', Context({'id': unique_id, 'type': thank_type, }))
    return HttpResponse(response)


def consumer(request):
    response = render(request, 'page/consumer.html')
    return HttpResponse(response)


def producer(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_id = form.process()
            url = reverse('thanks', args=['contact', contact_id])
            return HttpResponseRedirect(url)
        else:
            return HttpResponseRedirect('/')

    response = render(request, 'page/producer.html', Context({'form': ContactForm()}))
    return HttpResponse(response)


def faq(request):
    response = render(request, 'page/faq.html')
    return HttpResponse(response)
