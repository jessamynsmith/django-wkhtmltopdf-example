from django.views.generic.edit import FormView

from pdf_create.forms import PdfForm


class PdfCreateView(FormView):

    template_name = 'pdf_create/pdf_create.html'
    form_class = PdfForm
    success_url = '/'

    def form_valid(self, form):
        # Create PDF here
        return super(PdfCreateView, self).form_valid(form)
