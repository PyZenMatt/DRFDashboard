from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Document, Profile
from .serializers import DocumentSerializer, ProfileSerializer

class DocumentViewSet(ModelViewSet):
    """
    API endpoint per gestire i documenti.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ritorna solo i documenti dell'utente autenticato
        return Document.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Imposta l'utente autenticato come proprietario del documento
        serializer.save(user=self.request.user)


class ProfileViewSet(ModelViewSet):
    """
    API endpoint per gestire i profili utente.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ritorna solo il profilo dell'utente autenticato
        return Profile.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        # Salva il profilo dell'utente autenticato
        serializer.save(user=self.request.user)
