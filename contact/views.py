from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.template.loader import render_to_string

from .forms import ContactForm


def contact(request):

    cust_email = request.POST.get('contact_email')

    if request.method == 'POST':
        contact_form = {
            'name': request.POST.get('name'),
            'email': request.POST.get('contact_email'),
            'contact_as': request.POST.get('contact_as'),
            'message': request.POST.get('message')
        }
        subject = render_to_string(
            'contact/contact_emails/contact_email_subject.txt',
            {'contact': contact_form}
        )
        body = render_to_string(
            'contact/contact_emails/contact_email_body.txt',
            {'contact': contact_form}
        )
        send_mail(
            subject,
            body,
            cust_email,
            [settings.DEFAULT_FROM_EMAIL]
        )
        messages.success(
            request, 'Your message has been sent! \
                We will get back to you as soon as possible.')

    form = ContactForm

    context = {
        'form': form,
        'on_contact_page': True
    }

    return render(request, 'contact/contact.html', context)
