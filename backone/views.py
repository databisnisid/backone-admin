from django.shortcuts import render
from orbit.models import Orbit
from .models import BackOne
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse


def get_quota_current(request, ipaddress=None):
    q_current = 0
    try:
        backone = BackOne.objects.get(ipaddress=ipaddress)
        is_found = True if backone.orbit else False

    except ObjectDoesNotExist:
        is_found = False

    if is_found:
        orbit = Orbit.objects.get(id=backone.orbit.id)
        q_current_string = orbit.quota_current.split()
        q_current = float(q_current_string[0])

    return HttpResponse(q_current)


def get_quota_day(request, ipaddress=None):
    q_day = 0
    try:
        backone = BackOne.objects.get(ipaddress=ipaddress)
        is_found = True if backone.orbit else False

    except ObjectDoesNotExist:
        is_found = False

    if is_found:
        orbit = Orbit.objects.get(id=backone.orbit.id)
        q_day_string = orbit.quota_day.split()
        q_day = float(q_day_string[0])

    return HttpResponse(q_day)
