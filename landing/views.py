from django.shortcuts import render
from backone.models import BackOne
from django.conf import settings


def index(request):
    backone = BackOne.objects.all()
    #print(data)

    return render(request, 'index.html', {'backone': backone, 'settings': settings})
