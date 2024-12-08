from django.urls import path
from .views import (
    creer_membre,
    liste_membres,
    mettre_a_jour_membre,
    ajout_media,
    creer_emprunt,
    rentrer_emprunt,
    liste_medias,
    ajout_livre,
    retour_emprunt,
    bibliothecaire_home,
    ajouter_emprunt,
    ajouter_membre,
    media_list,
)

app_name = 'bibliothecaire'

urlpatterns = [
    path('', bibliothecaire_home, name='bibliothecaire_home'),
    path('membre/ajouter/', creer_membre, name='creer_membre'),
    path('membres/', liste_membres, name='liste_membres'),
    path('membre/modifier/<int:membre_id>/', mettre_a_jour_membre, name='modifier_membre'),
    path('medias/liste/', liste_medias, name='liste_medias'),
    path('medias/', liste_medias, name='liste_medias'),
    path('ajouter_media/', ajout_media, name='ajout_media'),
    path('media/ajouter/', ajout_media, name='ajouter_media'),
    path('emprunt/creer/', creer_emprunt, name='creer_emprunt'),
    path('emprunt/rentrer/<int:emprunt_id>/', rentrer_emprunt, name='rentrer_emprunt'),
    path('retour_emprunt', retour_emprunt, name='retour_emprunt'),
    path('livre/ajouter/', ajout_livre, name='ajouter_livre'),
    path('emprunt/ajouter/', ajouter_emprunt, name='ajouter_emprunt'),
    path('ajouter_membre/', ajouter_membre, name='ajouter_membre'),
    path('medias/', media_list, name='media_list'),
]