from django.shortcuts import render
from .models import Media



def list_medias(request):
    medias = Media.objects.all()
    return render(request, 'membre/list_medias.html', {'medias': medias})