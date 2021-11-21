from django import forms

class PochtaForma(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(max_length=250, required=False, widget=forms.Textarea)
