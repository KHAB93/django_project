
from django import forms
from .models import Membre, Media, Emprunt, Livre

class MembreForm(forms.ModelForm):
    class Meta:
        model = Membre
        fields = ['nom', 'email', 'adresse']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse'}),
        }

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['titre', 'auteur', 'date_publication', 'file', 'disponible']

class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['membre', 'media']  # Liste des champs à inclure dans le formulaire
        widgets = {
            'membre': forms.Select(attrs={'class': 'form-control'}),
            'media': forms.Select(attrs={'class': 'form-control'}),
        }

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['titre', 'auteur', 'date_publication']

class RetourEmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt  # Remplacez par votre modèle d'emprunt
        fields = ['id', 'date_retour']  # Ajoutez les champs nécessaires

class RetourEmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['id']