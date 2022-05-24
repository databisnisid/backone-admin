from django.shortcuts import render
from backone.models import BackOne


def index(request):
    backone = BackOne.objects.all()
    data = []
    for bo in backone:
        loc = bo.location.split(',')
        data.append({
            'name': bo.name,
            'lat': loc[0],
            'lng': loc[1]
        })

    #print(data)

    return render(request, 'index.html', {'data': data})
