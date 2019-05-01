from django.urls import path
from django.urls import path, include

from mail.views import MailView

urlpatterns=[
    path('', MailView.as_view()),

]