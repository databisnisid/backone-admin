from django.shortcuts import render
from backone.models import BackOne
from connection.models import ConnectionStatus
from django.conf import settings


def index(request):
    backone = BackOne.objects.all()
    cstatus = ConnectionStatus.objects.all()

    return render(request, 'statistic/index.html', {
        'backone': backone,
        'cstatus': cstatus,
        'settings': settings
    })
