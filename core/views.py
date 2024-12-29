from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Document
from .serializers import DocumentSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def document_list(request):
    documents = Document.objects.filter(user=request.user)
    return render(request, 'core/document_list.html')


@login_required
def document_upload(request):
    if request.method == 'POST':
        newdoc = Document(
            file=request.FILES['file'],
            user=request.user
        )
        newdoc.save()
        return HttpResponseRedirect(reverse('document_list'))
    return render(request, 'core/document_list.html')



class DocumentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows documents to be viewed or edited.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ensure a user sees only their own documents.
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Save the document with the current user.
        serializer.save(user=self.request.user)

