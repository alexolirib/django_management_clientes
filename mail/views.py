from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.core.mail import EmailMessage
# Create your views here.

#http://cheng.logdown.com/posts/2016/06/23/django-how-to-send-email-via-smtp
class MailView(View):
    def get(self, request, *args, **kwargs):
        email = EmailMessage(subject='email django do outlook',
                             body='testando email para o gmail',
                             to=['alexolirib@gmail.com'],
                             cc=['ribeirolx17@gmail.com'])
        email.send()
        return HttpResponse("deu certo")

    def post(self, request, *args, **kwargs):
        return HttpResponse("deu certo")