from django.db import models
from django.utils import timezone

class Membre(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    adresse = models.CharField(max_length=255)
    date_inscription = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nom


    def __str__(self):
        return self.nom

class Media(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    date_publication = models.DateField()
    file = models.FileField(upload_to='liste_medias/')
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titre

class Emprunt(models.Model):
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    date_emprunt = models.DateTimeField(default=timezone.now)
    date_retour = models.DateTimeField(null=True, blank=True)  # Champ pour la date de retour

    def __str__(self):
        return f"{self.membre} a emprunté {self.media}"

class Livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=100)
    date_publication = models.DateField()

    def __str__(self):
        return self.titre