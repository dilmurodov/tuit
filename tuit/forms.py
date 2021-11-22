from django import forms
from .models import Comments

class PochtaForma(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(max_length=250, required=False, widget=forms.Textarea)

# dinamicheskiy model buyicha Forma yaratish
class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'email', 'text')