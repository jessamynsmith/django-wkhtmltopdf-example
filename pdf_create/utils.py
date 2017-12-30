import os
import pdfkit

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


def get_full_domain():
    scheme = 'https'
    if not settings.SECURE_SSL_REDIRECT:
        scheme = 'http'
    return '%s://%s' % (scheme, Site.objects.get_current().domain)


def send_email(to_email, subject, context, text_template, html_template, attachments=[]):
    try:
        plaintext = get_template(text_template)
        text_body = plaintext.render(context)

        html_body = None
        if html_template:
            html = get_template(html_template)
            html_body = html.render(context)

        recipients = [to_email]
        msg = EmailMultiAlternatives(subject, text_body, to=recipients,
                                     reply_to=settings.REPLY_TO)
        if html_body:
            msg.attach_alternative(html_body, "text/html")

        for filename, content, mimetype in attachments:
            msg.attach(filename, content, mimetype)

        msg.send()
    except Exception as e:
        print(e)
    return True


def get_pdfkit_options():
    # Options for wkhtmltopdf
    # (see http://madalgo.au.dk/~jakobt/wkhtmltoxdoc/wkhtmltopdf-0.9.9-doc.html)
    options = {
        'footer-font-name': 'Verdana',
        'footer-font-size': '10',
        'footer-spacing': '5',
    }
    return options


def get_pdfkit_config():
    wkhtmltopdf = os.path.join(settings.BASE_DIR, 'bin', 'wkhtmltopdf')
    config = pdfkit.configuration(wkhtmltopdf=bytes(wkhtmltopdf, 'utf-8'))
    return config


def get_pdfkit_contents(rendered_template, extra_options={}):
    options = get_pdfkit_options()
    options.update(extra_options)
    return pdfkit.from_string(rendered_template, False, options=options,
                              configuration=get_pdfkit_config())
