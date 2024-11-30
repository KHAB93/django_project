
from django.urls import path
from .views import list_medias

urlpatterns = [
    path('medias/', list_medias, name='list_medias'),
]