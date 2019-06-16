from django.urls import path, include
from periodos.views import PeriodoListView
urlpatterns=[
     path('list/', PeriodoListView.as_view(), name='periodo_search'),
]