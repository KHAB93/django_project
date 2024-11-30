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


)

urlpatterns = [
    path('', liste_medias, name='listeMedias'),
    path('membre/ajouter/', creer_membre, name='ajouter_membre'),
    path('membres/', liste_membres, name='liste_membres'),
    path('membre/modifier/<int:membre_id>/', mettre_a_jour_membre, name='modifier_membre'),
    path('medias/', liste_medias, name='liste_medias'),
    path('media/ajouter/', ajout_media, name='ajouter_media'),
    path('emprunt/creer/', creer_emprunt, name='creer_emprunt'),
    path('emprunt/rentrer/<int:emprunt_id>/', rentrer_emprunt, name='rentrer_emprunt'),
    path('emprunt/retour/', retour_emprunt, name='retour_emprunt'),
    path('livres/', liste_medias, name='liste_livres'),
    path('livre/ajouter/', ajout_livre, name='ajouter_livre'),
    path('ajout_media/', ajout_media, name='ajout_media'),
    path('creer/', creer_membre, name='creer_membre'),

]
