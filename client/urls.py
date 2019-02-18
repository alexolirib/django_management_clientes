
from django.urls import path

from client.views import persons_list, persons_new, persons_update, persons_delete, PersonList, PersonDetail

urlpatterns = [
    path('list/', persons_list, name='person_list'),
    path('new/', persons_new, name='person_new'),
    path('update/<int:id>/', persons_update, name='person_update'),
    path('delete/<int:id>', persons_delete, name='person_delete'),
    path('person_list/', PersonList.as_view()),
    path('person_details/<int:pk>/', PersonDetail.as_view(), name="person_detail_cbv"),
]
