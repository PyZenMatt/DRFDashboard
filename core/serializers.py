from rest_framework import serializers
from .models import Document, Profile

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'name', 'file', 'created_at']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'date_of_birth', 'residence', 'bio', 'hair_color', 'photo']
