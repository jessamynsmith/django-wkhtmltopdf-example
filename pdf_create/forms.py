from django import forms


class PdfForm(forms.Form):
    email = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
