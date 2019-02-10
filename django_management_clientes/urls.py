from django.contrib import admin
from django.urls import path, include
from client import urls as clients_urls

urlpatterns = [
    path('client/', include(clients_urls)),
    path('admin/', admin.site.urls),
]