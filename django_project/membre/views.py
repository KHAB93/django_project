from django.shortcuts import render
from .models import Media

def membre_view(request):
    return render(request, 'membre/home.html')

def list_medias(request):
    medias = Media.objects.all()
    return render(request, 'liste_medias.html', {'medias': medias})

