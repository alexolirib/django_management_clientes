from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from client import urls as clients_urls
from home import urls as home_urls

urlpatterns = [
    path('client/', include(clients_urls)),
    path('', include(home_urls)),
    #login - django já prover toda a parte de segurança do app
    path('login/', auth_views.login, name='login'),
    #para personalzar o logout vou fazer isso no app Home
    #path('logout/', auth_views.logout, name='logout'),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) = visualizar imagem

