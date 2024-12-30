from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateField(null=True, blank=True)  # Campo per la data di nascita
    residence = models.CharField(max_length=255, blank=True)  # Campo per la residenza
    bio = models.TextField(max_length=500, blank=True)  # Biografia
    hair_color = models.CharField(max_length=50, blank=True)  # Colore dei capelli
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)  # Foto del profilo
    custom_field = models.TextField(blank=True)  # Campo personalizzato (ad esempio hobby o interessi)

    def __str__(self):
        return f"{self.user.username}'s Profile"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
