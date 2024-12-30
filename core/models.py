from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateField(null=True, blank=True)
    residence = models.CharField(max_length=255, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    hair_color = models.CharField(max_length=50, blank=True)
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
