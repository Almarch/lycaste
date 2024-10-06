from django import forms
from main.models import Taxon

class TaxonForm(forms.ModelForm):
    class Meta:
        model = Taxon
        fields = '__all__'