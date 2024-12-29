from django import forms
from .models import Document
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'photo']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file', 'name']  # Aggiungi 'name' se è un campo nel tuo modello Document
