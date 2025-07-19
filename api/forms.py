from django import forms
from .models import Ordonnance

class OrdonnanceUploadForm(forms.ModelForm):
    class Meta:
        model = Ordonnance
        fields = ['image']