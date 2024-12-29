from django.contrib import admin
from .models import Document, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')  # Mostra l'utente e la bio nella lista
    search_fields = ('user__username', 'bio')  # Aggiungi una barra di ricerca

# Opzionale: definisci una classe Admin per personalizzare l'interfaccia admin
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'created_at']  # Campi da mostrare nell'elenco
    search_fields = ['name', 'user__username']  # Campi per la ricerca
    list_filter = ['created_at']  # Filtri disponibili

# Registra il modello con l'admin
admin.site.register(Document, DocumentAdmin)


# Register your models here.
