import re
from datetime import datetime, date
from .models import Orbit, OrbitMulti, OrbitStatQuota
from connector.drivers import orbit, orbit_multi
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from notification.telegram import send_notification_telegram


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

def check_quota_orbit(current, day):
    NOTIF_Q_GB = 5
    NOTIF_Q_DAY = 5

    q_split = current.replace("GB", "")
    q_gb = float(q_split)
    q_day = 0
    if day:
        q_split = day.replace("Hari", "")
        q_day = float(q_split)
    q_gb_status = True if q_gb > NOTIF_Q_GB else False
    q_day_status = True if q_day > NOTIF_Q_DAY else False

    #print(q_gb_status, q_gb, q_day_status, q_day)
    return q_gb_status, q_day_status


'''
def send_notification_telegram(title, message):
    event = {
        'title':  title,
        'description': message,
        'start_date': timezone.now()
    }
    post_event_on_telegram(event)
'''


def check_quota_orbit_notification_daily():
    #orbits = Orbit.objects.filter().order_by('updated_at')
    orbits = Orbit.objects.all()

    result_gb = []
    result_day = []
    for o in orbits:
        print(o.username, o.password)
        if o.username != 'nopass@backone.cloud' or o.password != 'nopassword':
            q_gb_ok, q_day_ok = check_quota_orbit(o.quota_current, o.quota_day)
            print(o.msisdn, q_gb_ok, o.quota_current, q_day_ok, o.quota_day)

            if not q_gb_ok:
                print('WARNING GB', o.msisdn)
                result_gb.append(o.msisdn)
            if not q_day_ok:
                print('WARNING DAY', o.msisdn)
                result_day.append(o.msisdn)

    if result_gb:
        print(result_gb)
        description = '\n'.join([msisdn for msisdn in result_gb])
    else:
        description = 'Tidak Ada'
    send_notification_telegram('Orbit GB kurang dari 5 GB', description)

    if result_day:
        print(result_day)
        description = '\n'.join([msisdn for msisdn in result_day])
    else:
        description = 'Tidak Ada'
    send_notification_telegram('Orbit DAY kurang dari 5 Hari', description)


def get_all_quota_orbit():
    orbits = Orbit.objects.filter().order_by('updated_at')

    for o in orbits:
        print(o.username, o.password)
        if o.username != 'nopass@backone.cloud' or o.password != 'nopassword':
            q_current, q_total, q_day = orbit.get_quota(o.username, o.password)
            o.quota_current = q_current if len(q_current) != 0 else o.quota_current
            o.quota_total = q_total if len(q_total) != 0 else o.quota_total
            o.quota_day = q_day if len(q_day) != 0 else o.quota_day
            o.save()
            print(timezone.now(), o.msisdn, o.quota_current, o.quota_total, o.quota_day)


def string_to_int(s):
    return int(''.join(c for c in s if c.isdigit()))


def split_quota_multi(quota):
    q = quota.split('/')
    return q[0].strip(), q[1].strip()


def quota_int(quota):
    if '/' in quota: 
        quota, quota_c = split_quota_multi(quota)

    if 'GB' in quota:
        quota_f = float(quota.replace('GB', ''))
        quota_f = quota_f * 1024

    if 'MB' in quota:
        quota_f = float(quota.replace('MB', ''))

    return int(quota_f)


def get_all_quota_orbit_multi():
    username = 'orbitzte@backone.cloud'
    password = 'Orbit8899!'
    result = orbit_multi.get_quota_multi(username, password)
    #result = OM.get_quota_multi(username, password)

    for msisdn, val in result.items():
        q_current, q_total = split_quota_multi(val[0])
        q_day = None
        if val[1]:
            from datetime import datetime, date
            date_split = val[1].split('-')
            d_next = date(int(date_split[2]), int(date_split[1]), int(date_split[0]))
            d_curr = date.today()
            d_delta = d_next - d_curr
            q_day = str(d_delta.days) + ' Hari'

        print(msisdn, q_current, q_total, q_day)

        try:
            om = OrbitMulti.objects.get(msisdn=msisdn)
        except ObjectDoesNotExist:
            om = OrbitMulti()

        om.username = username
        om.password = password
        om.msisdn = msisdn
        om.quota_current = q_current
        om.quota_total = q_total
        om.quota_day = q_day
        om.save()


def check_quota_orbit_multi_notification_daily():
    #orbits = Orbit.objects.filter().order_by('updated_at')
    orbits = OrbitMulti.objects.all()

    result_gb = []
    result_day = []
    for o in orbits:
        print(o.username, o.password)
        if o.username != 'nopass@backone.cloud' or o.password != 'nopassword':
            q_gb_ok, q_day_ok = check_quota_orbit(o.quota_current, o.quota_day)
            print(o.msisdn, q_gb_ok, o.quota_current, q_day_ok, o.quota_day)

            if not q_gb_ok:
                print('WARNING GB', o.msisdn)
                result_gb.append(o.msisdn)
            if not q_day_ok:
                print('WARNING DAY', o.msisdn)
                result_day.append(o.msisdn)

    if result_gb:
        print(result_gb)
        description = '\n'.join([msisdn for msisdn in result_gb])
    else:
        description = 'Tidak Ada'
    send_notification_telegram('OrbitMulti GB kurang dari 5 GB', description)

    if result_day:
        print(result_day)
        description = '\n'.join([msisdn for msisdn in result_day])
    else:
        description = 'Tidak Ada'
    send_notification_telegram('OrbitMulti DAY kurang dari 5 Hari', description)


def check_selenium_working():
    orbit = Orbit.objects.order_by('updated_at').last()
    current_time = timezone.now()
    delta_time = current_time - orbit.updated_at

    if delta_time.days > 1:
        description = 'Pengecheckan Orbit terlambat lebih dari 1 hari! Segera check BackOne Data!'
    else:
        description = 'Pengecheckan Orbit Aman'
    send_notification_telegram('Pengecheckan Orbit', description)

    orbit = OrbitMulti.objects.order_by('updated_at').last()
    current_time = timezone.now()
    delta_time = current_time - orbit.updated_at

    if delta_time.days > 1:
        description = 'Pengecheckan Orbit Multi terlambat lebih dari 1 hari! Segera check BackOne Data!'
    else:
        description = 'Pengecheckan Orbit Multi Aman'
    send_notification_telegram('Pengecheckan Orbit', description)


def orbit_stat_worker():
    ''' Start every midnite'''

    orbits = Orbit.objects.all()

    for orbit in orbits:
        msisdn = re.sub('^0', '62', quota.msisdn)
        quota = quota_int(orbit.quota_current)
        OrbitStatQuota.objects.create(msisdn=msisd, quota=quota)

    orbits = OrbitMulti.objects.all()

    for orbit in orbits:
        msisdn = re.sub('^0', '62', quota.msisdn)
        quota = quota_int(orbit.quota_current)
        OrbitStatQuota.objects.create(msisdn=msisd, quota=quota)


