from django.db import models

class Media(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    date_publication = models.DateField()
    file = models.FileField(upload_to='list_Medias/')
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titre