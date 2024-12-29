from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Document
from .serializers import DocumentSerializer
from django.contrib.auth.decorators import login_required
from .forms import DocumentForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('document_list')  # Puoi sostituire con una pagina personale
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'core/edit_profile.html', {'form': form})

@login_required
def document_list(request):
    documents = Document.objects.filter(user=request.user)
    return render(request, 'core/document_list.html', {'documents':documents})


@login_required
def document_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = form.save(commit=False)
            newdoc.user = request.user
            newdoc.save()
            return redirect('document_list')  # Usa 'redirect' per una gestione più pulita degli URL
    else:
        form = DocumentForm()  # Crea un form vuoto per il GET

    return render(request, 'core/document_upload.html', {'form': form})
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

