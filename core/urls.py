from django.urls import path
from .views import document_list, document_upload  # Assicurati di importare le funzioni correttamente

urlpatterns = [
    path('documents/', document_list, name='core/document_list'),  # URL per la visualizzazione della lista dei documenti
    path('documents/upload/', document_upload, name='document_upload'),  # URL per il caricamento dei documenti
]
