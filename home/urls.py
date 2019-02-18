from django.urls import path
from home.views import home, my_logout, HomePageView, MyView
#templates views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', home, name='tela_home'),
    path('logout/', my_logout, name='logout'),
    #posso fazer isso quando quero mostrar um arquivo html static
    #partir daqui é possível utilizar classe
    path('home2/', TemplateView.as_view(template_name='home2.html'), name='home2'),
    #para conseguir mandar parâmetros
    path('home3/', HomePageView.as_view(template_name='home3.html'), name='home3'),
    #utilizar para views bem básicas
    path('view/', MyView.as_view())

]