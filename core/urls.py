from django.urls import path
from .views import edit_profile, document_list, document_upload

urlpatterns = [
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('documents/', document_list, name='document_list'),  # URL per la visualizzazione della lista dei documenti
    path('documents/upload/', document_upload, name='document_upload'),  # URL per il caricamento dei documenti
]
