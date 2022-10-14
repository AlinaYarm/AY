from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from core import models

def index(request):
    #now = timezone.now()
    person = models.Person.objects.first()
    #response = HttpResponse(f'<h1>Hello World!<h1>{now}')
    response = render(request, 'core/index.html', context={'person': person})
    return response

