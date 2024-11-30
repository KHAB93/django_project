# membre/forms.py
from django import forms

class CommentaireForm(forms.Form):
    nom = forms.CharField(max_length=100, label='Votre nom')
    email = forms.EmailField(label='Votre email')
    commentaire = forms.CharField(widget=forms.Textarea, label='Votre commentaire')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Ce champ est requis.")
        return email