from django.urls import path
from home.views import home, my_logout

urlpatterns = [
    path('', home, name='tela_home'),
    path('logout/', my_logout, name='logout')
]