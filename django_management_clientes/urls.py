from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from client import urls as clients_urls


urlpatterns = [
    path('client/', include(clients_urls)),
    #login - django já prover toda a parte de segurança do app
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) = visualizar imagem

