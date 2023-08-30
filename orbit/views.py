from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from django.core.exceptions import ObjectDoesNotExist
from .models import Orbit, OrbitMulti


def get_quota_all_orbit(request):
    return JsonResponse(list(Orbit.objects.all().values()), safe=False)


def get_quota_all_orbit_multi(request):
    return JsonResponse(list(OrbitMulti.objects.all().values()), safe=False)


def get_quota(request, msisdn):

    qs = Orbit.objects.filter(msisdn__contains=msisdn)

    if not qs:
        qs = OrbitMulti.objects.filter(msisdn__contains=msisdn)

    print(msisdn, qs)
    serialized_qs = serialize('python', qs)
    return JsonResponse(serialized_qs, safe=False)






