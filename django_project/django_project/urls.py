from django.contrib import admin
from django.urls import path, include
from .views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('bibliothecaire/', include('bibliothecaire.urls', namespace='bibliothecaire')),
    path('membre/', include('membre.urls')),
]