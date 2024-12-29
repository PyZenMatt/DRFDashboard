from django.contrib import admin
from .models import Document  # Importa il modello Document dalla tua app

# Opzionale: definisci una classe Admin per personalizzare l'interfaccia admin
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'created_at']  # Campi da mostrare nell'elenco
    search_fields = ['name', 'user__username']  # Campi per la ricerca
    list_filter = ['created_at']  # Filtri disponibili

# Registra il modello con l'admin
admin.site.register(Document, DocumentAdmin)


# Register your models here.
