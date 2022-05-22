from .models import Orbit
from connector.drivers import orbit


def get_all_quota_orbit():
    orbits = Orbit.objects.all()

    for o in orbits:
        q_current, q_total, q_day = orbit.get_quota(o.username, o.password)
        o.quota_current = q_current if len(q_current) != 0 else o.quota_current
        o.quota_total = q_total if len(q_total) != 0 else o.quota_total
        o.quota_day = q_day if len(q_day) != 0 else o.quota_day
        o.save()
        print(o.quota_current, o.quota_total, o.quota_day)
