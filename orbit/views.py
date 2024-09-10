from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from django.core.exceptions import ObjectDoesNotExist
from .models import Orbit, OrbitMulti
from dsc.models import DscDpi


def get_quota_all_orbit(request):
    return JsonResponse(list(Orbit.objects.all().values(
        'id', 'msisdn', 'quota_total', 'quota_current', 'quota_day', 'quota_prev', 'updated_at', 'quota_type'
        )), safe=False)


def get_quota_all_orbit_multi(request):
    return JsonResponse(list(OrbitMulti.objects.all().values(
        'id', 'msisdn', 'quota_total', 'quota_current', 'quota_day', 'quota_prev', 'updated_at', 'quota_type'
        )), safe=False)


def get_quota(request, msisdn):

    qs = Orbit.objects.filter(msisdn__contains=msisdn).values(
            'id', 'msisdn', 'quota_total', 'quota_current', 'quota_day', 'quota_prev', 'updated_at', 'quota_type'
            )

    if not qs:
        qs = OrbitMulti.objects.filter(msisdn__contains=msisdn).values(
                'id', 'msisdn', 'quota_total', 'quota_current', 'quota_day', 'quota_prev', 'updated_at', 'quota_type'
                )

    if not qs:
        qs = DscDpi.objects.filter(msisdn__contains=msisdn).values(
                'id', 'msisdn', 'quota_total', 'quota_current', 'quota_day', 'quota_prev', 'updated_at', 'quota_type'
                )

    print(msisdn, qs)
    return JsonResponse(list(qs), safe=False)






