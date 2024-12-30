from django import forms
from .models import Document, Profile
from allauth.account.forms import SignupForm
from django.contrib.auth.models import User

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, required=True, label="Nome")
    last_name = forms.CharField(max_length=30, required=True, label="Cognome")
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}), label="Data di nascita")
    residence = forms.CharField(max_length=255, required=False, label="Residenza")

    def save(self, request):
        # Salva l'utente base
        user = super().save(request)
        
        # Aggiungi nome e cognome al modello User
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        # Il segnale post_save si occuperà della creazione del profilo
        user.profile.date_of_birth = self.cleaned_data['date_of_birth']
        user.profile.residence = self.cleaned_data['residence']
        user.profile.save()

        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'photo']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file', 'name']  # Aggiungi 'name' se è un campo nel tuo modello Document
