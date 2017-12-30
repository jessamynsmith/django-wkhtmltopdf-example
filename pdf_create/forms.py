from django import forms


class PdfForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
