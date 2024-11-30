from django.shortcuts import render, redirect, get_object_or_404
from .models import Membre, Media, Emprunt, Livre
from .forms import MembreForm, MediaForm, EmpruntForm, LivreForm, RetourEmpruntForm
from django.utils import timezone
from datetime import timedelta



def creer_membre(request):
    if request.method == 'POST':
        form = MembreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_membres')
    else:
        form = MembreForm()
    return render(request, 'bibliothecaire/creer_membre.html', {'form': form})


def liste_membres(request):
    membres = Membre.objects.all()
    return render(request, 'bibliothecaire/liste_membres.html', {'membres': membres})


def mettre_a_jour_membre(request, membre_id):
    membre = get_object_or_404(Membre, id=membre_id)
    if request.method == 'POST':
        form = MembreForm(request.POST, instance=membre)
        if form.is_valid():
            form.save()
            return redirect('liste_membres')
    else:
        form = MembreForm(instance=membre)
    return render(request, 'bibliothecaire/modifier_membre.html', {'form': form})

def ajouter_membre(request):
    if request.method == 'POST':
        form = MembreForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigez vers la liste des membres ou une autre page
    else:
        form = MembreForm()
    return render(request, 'bibliothecaire/ajouter_membre.html', {'form': form})

def liste_medias(request):
    medias = Media.objects.all()
    return render(request, 'bibliothecaire/liste_medias.html', {'medias': medias})


def ajout_media(request):
    if request.method == 'POST':
        form = MediaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_medias')
    else:
        form = MediaForm()
    return render(request, 'bibliothecaire/ajouter_media.html', {'form': form})


def creer_emprunt(request):
    if request.method == 'POST':
        form = EmpruntForm(request.POST)
        if form.is_valid():
            emprunt = form.save(commit=False)

            if emprunt.media.type == 'jeu_de_plateau':
                form.add_error(None, "Les jeux de plateaux ne peuvent pas être empruntés.")
            else:
                # This line needs to be indented
                nombre_emprunts_actifs = Emprunt.objects.filter(
                    membre=emprunt.membre,
                    date_retour__isnull=True
                ).count()

                emprunts_en_retard = Emprunt.objects.filter(
                    membre=emprunt.membre,
                    date_retour__isnull=True,
                    date_emprunt__lt=timezone.now() - timedelta(weeks=1)
                ).exists()

                if emprunts_en_retard:
                    form.add_error(None, "Ce membre a un emprunt en retard et ne peut pas emprunter de nouveaux médias.")
                elif nombre_emprunts_actifs < 3:
                    emprunt.save()
                    return redirect('liste_medias')
                else:
                    form.add_error(None,
                                   "Ce membre a déjà 3 emprunts actifs. Veuillez retourner un emprunt avant d'en faire un nouveau.")
    else:
        form = EmpruntForm()
    return render(request, 'bibliothecaire/ajouter_emprunt.html', {'form': form})


def rentrer_emprunt(request, emprunt_id):
    emprunt = get_object_or_404(Emprunt, id=emprunt_id)
    if request.method == 'POST':
        form = EmpruntForm(request.POST, instance=emprunt)
        if form.is_valid():
            form.save()
            return redirect('liste_medias')
    else:
        form = EmpruntForm(instance=emprunt)
    return render(request, 'bibliothecaire/retour_emprunt.html', {'form': form, 'emprunt': emprunt})

def retour_emprunt(request):
    if request.method == 'POST':
        form = RetourEmpruntForm(request.POST)
        if form.is_valid():
            emprunt = get_object_or_404(Emprunt, id=form.cleaned_data['id'])

            if timezone.now() > (emprunt.date_emprunt + timedelta(weeks=1)):

                form.add_error(None, "L'emprunt ne peut pas être retourné après une semaine.")
            else:
                emprunt.date_retour = timezone.now()
                emprunt.save()
                return redirect('liste_medias')
    else:
        form = RetourEmpruntForm()

    return render(request, 'retour_emprunt.html', {'form': form})

def liste_medias(request):
    livres = Livre.objects.all()
    return render(request, 'bibliothecaire/liste_medias.html', {'livres': livres})


def ajout_livre(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_medias')
    else:
        form = LivreForm()
    return render(request, 'bibliothecaire/ajouter_livre.html', {'form': form})




