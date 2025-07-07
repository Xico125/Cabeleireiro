from django.contrib import admin
from django.urls import path
from core import views as core_views
from cortes import views as cortes_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('sobre/', core_views.sobre, name='sobre'),
    path('contactos/', core_views.contactos, name='contactos'),
    path('exemplos/', cortes_views.exemplos, name='exemplos'),
]

# Para carregar imagens no modo de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)