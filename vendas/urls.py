from django.urls import path, include
from vendas.views import DashboardView

urlpatterns = [
     path('dashboard/', DashboardView.as_view(), name='person_list'),
]
