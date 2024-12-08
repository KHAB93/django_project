from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def membre_home(request):
    return render(request, 'membre_home.html')

def bibliothecaire_home(request):
    return render(request, 'bibliothecaire_home.html')

def home(request):
    return render(request, 'home.html')

def ajouter_emprunt(request):
    return render(request, 'ajouter_emprunt.html')

def ajouter_media(request):
    return render(request, 'ajouter_media.html')

def creer_membre(request):
    return render(request, 'creer_membre.html')

def liste_medias(request):
    return render(request, 'liste_medias.html')

def liste_membres(request):
    return render(request, 'liste_membres.html')

def modifier_membre(request, id):
    return render(request, 'modifier_membre.html', {'id': id})

def retour_emprunt(request):
    return render(request, 'retour_emprunt.html')