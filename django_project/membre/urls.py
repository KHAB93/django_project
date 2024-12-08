
from django.urls import path
from .views import list_medias, membre_view


urlpatterns = [
    path('', membre_view, name='membre_home'),
    path('medias/', list_medias, name='list_medias'),
]