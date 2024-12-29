from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file', 'name']  # Aggiungi 'name' se è un campo nel tuo modello Document
