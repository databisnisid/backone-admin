from .models import Orbit
from connector.drivers import orbit
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone


def get_quota_orbit(msisdn):

    if msisdn is not None:
        try:
            o = Orbit.objects.get(msisdn=msisdn)

            if o.username != 'nopass@backone.cloud' or o.password != 'nopassword':
                q_current, q_total, q_day = orbit.get_quota(o.username, o.password)
                o.quota_current = q_current if len(q_current) != 0 else o.quota_current
                o.quota_total = q_total if len(q_total) != 0 else o.quota_total
                o.quota_day = q_day if len(q_day) != 0 else o.quota_day
                o.save()
                print(o.msisdn, o.quota_current, o.quota_total, o.quota_day)

        except ObjectDoesNotExist:
            print('Object is not found!')


def get_all_quota_orbit():
    orbits = Orbit.objects.filter().order_by('updated_at')

    for o in orbits:
        if o.username != 'nopass@backone.cloud' or o.password != 'nopassword':
            q_current, q_total, q_day = orbit.get_quota(o.username, o.password)
            o.quota_current = q_current if len(q_current) != 0 else o.quota_current
            o.quota_total = q_total if len(q_total) != 0 else o.quota_total
            o.quota_day = q_day if len(q_day) != 0 else o.quota_day
            o.save()
            print(timezone.now, o.msisdn, o.quota_current, o.quota_total, o.quota_day)
