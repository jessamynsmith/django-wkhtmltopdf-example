import os

from django.conf import settings
from django.contrib import messages
from django.template.defaultfilters import date
from django.template.loader import get_template
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.views.generic.edit import FormView

from pdf_create.forms import PdfForm
from pdf_create.utils import get_full_domain, get_pdfkit_contents, send_email


class PdfCreateView(FormView):
    RESUME_EXTENSION = '.pdf'

    template_name = 'pdf_create/pdf_create.html'
    form_class = PdfForm
    success_url = '/'

    def form_valid(self, form):
        date_created = date(timezone.now())

        title = 'Example PDF - {}'.format(date_created)

        css_content = ''
        static_dir = os.path.join(settings.PROJECT_DIR, 'static')
        css_files = [
            os.path.join('css', 'base.css'),
        ]
        for file_path in css_files:
            with open(os.path.join(static_dir, file_path)) as css_file:
                css_content = '{}\n{}'.format(css_content, css_file.read())
        context = {
            'title': title,
            'css_content': css_content,
            'formatted_text': form.cleaned_data['message'],
            'admin_name': settings.ADMINS[0][0],
            'full_domain': get_full_domain(),
        }
        html = get_template('pdf_create/pdf.html')
        rendered_resume = html.render(context)

        base_filename = '{}'.format(_('example'))
        timestamp = str(timezone.now()).split('.')[0]
        filename = '{} {}{}'.format(base_filename, timestamp, self.RESUME_EXTENSION)

        # Options for wkhtmltopdf (see http://madalgo.au.dk/~jakobt/wkhtmltoxdoc/wkhtmltopdf-0.9.9-doc.html)
        extra_options = {}
        extra_options['footer-left'] = u'{} {}'.format(_('Created: '), date_created)
        extra_options['footer-right'] = u'{} [page] {} [toPage]'.format(_('Page'), _('of'))

        pdf_contents = get_pdfkit_contents(rendered_resume, extra_options=extra_options)

        # with open('{}.html'.format(filename), 'w') as html_file:
        #     html_file.write(str(rendered_resume))
        #
        # with open(filename, 'wb') as pdf_file:
        #     pdf_file.write(pdf_contents)

        to_email = form.cleaned_data['email']
        template_name = 'pdf_created'
        plaintext = 'pdf_create/email/%s.txt' % template_name
        html = 'pdf_create/email/%s.html' % template_name
        attachments = [(filename, pdf_contents, 'application/pdf')]
        send_email(to_email, _('You created a PDF!'), context, plaintext, html,
                   attachments)

        messages.success(self.request, _('PDF generated and emailed.'))
        return super(PdfCreateView, self).form_valid(form)
