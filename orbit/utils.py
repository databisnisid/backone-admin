from os import walk
import re
from datetime import datetime, date
from .models import Orbit, OrbitMulti, OrbitStatQuota
from connector.drivers import orbit, orbit_multi
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.conf import settings
from notification.telegram import send_notification_telegram
import logging

# Basic configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


NOTIF_Q_GB = settings.NOTIF_Q_GB
NOTIF_Q_DAY = settings.NOTIF_Q_DAY


def quota_day_normalize(text: str) -> str:
    d_curr = datetime.today()
    this_y = str(d_curr.year)
    next_y = str(d_curr.year + 1)
    if this_y in text or next_y in text:
        text_split = text.split()
        date_string = f"{text_split[-3]} {text_split[-2]} {text_split[-1]}"
        d_object = datetime.strptime(date_string, "%d %b %Y")
        d_curr = datetime.today()
        d_delta = d_object - d_curr
        q_day = str(d_delta.days) + " Hari"
    else:
        q_day = ""

    return q_day


def get_quota_orbit(msisdn):

    driver = orbit.driver_start()

    if msisdn is not None:
        try:
            o = Orbit.objects.get(msisdn=msisdn)

            if o.username != "nopass@backone.cloud" or o.password != "nopassword":
                # q_current, q_total, q_day = orbit.get_quota(o.username, o.password)
                q_current, q_total, q_day, error_msg = orbit.get_quota(
                    o.username, o.password, driver
                )
                # o.quota_current = q_current if len(q_current) != 0 else o.quota_current
                # o.quota_total = q_total if len(q_total) != 0 else o.quota_total
                # o.quota_day = q_day if len(q_day) != 0 else o.quota_day
                o.quota_current = q_current if len(q_current) != 0 else None
                o.quota_total = q_total if len(q_total) != 0 else None
                o.quota_day = quota_day_normalize(q_day) if len(q_day) != 0 else None

                """ Only save when there is data from Orbit website """
                if o.quota_current and o.quota_total and o.quota_day:
                    o.save()
                # print(o.msisdn, o.quota_current, o.quota_total, o.quota_day)
                logging.info(
                    f"{o.msisdn} {o.quota_current} {o.quota_total} {o.quota_day}"
                )

        except ObjectDoesNotExist:
            logging.info("Object is not found!")

    orbit.driver_quit(driver)


def check_quota_orbit(current, day):
    # NOTIF_Q_GB = 5
    # NOTIF_Q_DAY = 5
    # NOTIF_Q_GB = settings.NOTIF_Q_GB
    # NOTIF_Q_DAY = settings.NOTIF_Q_DAY

    q_split = current.replace("GB", "")
    q_gb = float(q_split)
    q_day = 0
    if day:
        q_split = day.replace("Hari", "")
        q_day = float(q_split)
    q_gb_status = True if q_gb > NOTIF_Q_GB else False
    q_day_status = True if q_day > NOTIF_Q_DAY else False

    # print(q_gb_status, q_gb, q_day_status, q_day)
    return q_gb_status, q_day_status


"""
def send_notification_telegram(title, message):
    event = {
        'title':  title,
        'description': message,
        'start_date': timezone.now()
    }
    post_event_on_telegram(event)
"""


def check_quota_orbit_notification_daily():
    # orbits = Orbit.objects.filter().order_by('updated_at')
    orbits = Orbit.objects.all()

    result_gb = []
    result_day = []
    for o in orbits:
        print(o.username, o.password)
        if o.username != "nopass@backone.cloud" or o.password != "nopassword":
            q_gb_ok, q_day_ok = check_quota_orbit(o.quota_current, o.quota_day)
            print(o.msisdn, q_gb_ok, o.quota_current, q_day_ok, o.quota_day)

            if not q_gb_ok:
                print("WARNING GB", o.msisdn)
                result_gb.append(o.msisdn)
            if not q_day_ok:
                print("WARNING DAY", o.msisdn)
                result_day.append(o.msisdn)

    if result_gb:
        print(result_gb)
        description = "\n".join([msisdn for msisdn in result_gb])
    else:
        description = "Tidak Ada"
    send_notification_telegram(
        "Orbit GB kurang dari " + str(NOTIF_Q_GB) + " GB", description
    )

    if result_day:
        print(result_day)
        description = "\n".join([msisdn for msisdn in result_day])
    else:
        description = "Tidak Ada"
    send_notification_telegram(
        "Orbit DAY kurang dari " + str(NOTIF_Q_DAY) + " Hari", description
    )


def get_all_quota_orbit():
    orbits = Orbit.objects.filter().order_by("updated_at")

    """ Start Webdriver """
    # driver = orbit.driver_start()

    for o in orbits:
        print(o.username, o.password)
        if o.username != "nopass@backone.cloud" or o.password != "nopassword":
            # q_current, q_total, q_day = orbit.get_quota(o.username, o.password)
            driver = orbit.driver_start()
            q_current, q_total, q_day, error_msg = orbit.get_quota(
                o.username, o.password, driver
            )
            orbit.driver_quit(driver)
            # o.quota_current = q_current if len(q_current) != 0 else o.quota_current
            # o.quota_total = q_total if len(q_total) != 0 else o.quota_total
            # o.quota_day = q_day if len(q_day) != 0 else o.quota_day
            o.quota_current = q_current if len(q_current) != 0 else None
            o.quota_total = q_total if len(q_total) != 0 else None
            o.quota_day = quota_day_normalize(q_day) if len(q_day) != 0 else None
            o.error_msg = error_msg

            """ Only save when there is data from Orbit website """
            if o.quota_current and o.quota_total and o.quota_day:
                o.save()

            # print(timezone.now(), o.msisdn, o.quota_current, o.quota_total, o.quota_day)
            logging.info(
                f"{o.msisdn} {o.quota_current} {o.quota_total} {o.quota_day} {error_msg}"
            )

    """ Quit Webdriver """
    # orbit.driver_quit(driver)


def string_to_int(s):
    return int("".join(c for c in s if c.isdigit()))


def split_quota_multi(quota):
    q = quota.split("/")
    return q[0].strip(), q[1].strip()


def quota_int(quota):
    if "/" in quota:
        quota, quota_c = split_quota_multi(quota)

    if "GB" in quota:
        quota_f = float(quota.replace("GB", ""))
        quota_f = quota_f * 1024

    if "MB" in quota:
        quota_f = float(quota.replace("MB", ""))

    return int(quota_f)


def get_all_quota_orbit_multi():
    username = "orbitzte@backone.cloud"
    password = "Orbit8899!"
    result = orbit_multi.get_quota_multi(username, password)
    # result = OM.get_quota_multi(username, password)

    for msisdn, val in result.items():
        q_current, q_total = split_quota_multi(val[0])
        q_day = None
        if val[1]:
            # from datetime import datetime, date

            date_split = val[1].split("-")
            d_next = date(int(date_split[2]), int(date_split[1]), int(date_split[0]))
            d_curr = date.today()
            d_delta = d_next - d_curr
            q_day = str(d_delta.days) + " Hari"

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

            logging.info(f"{msisdn} {q_current} {q_total} {q_day} -> Saved!")
        else:
            logging.info(f"{msisdn} {q_current} {q_total} {q_day} -> NOT Saved!")


def check_quota_orbit_multi_notification_daily():
    # orbits = Orbit.objects.filter().order_by('updated_at')
    orbits = OrbitMulti.objects.all()

    result_gb = []
    result_day = []
    for o in orbits:
        print(o.username, o.password)
        if o.username != "nopass@backone.cloud" or o.password != "nopassword":
            q_gb_ok, q_day_ok = check_quota_orbit(o.quota_current, o.quota_day)
            print(o.msisdn, q_gb_ok, o.quota_current, q_day_ok, o.quota_day)

            if not q_gb_ok:
                print("WARNING GB", o.msisdn)
                result_gb.append(o.msisdn)
            if not q_day_ok:
                print("WARNING DAY", o.msisdn)
                result_day.append(o.msisdn)

    if result_gb:
        print(result_gb)
        description = "\n".join([msisdn for msisdn in result_gb])
    else:
        description = "Tidak Ada"
    send_notification_telegram(
        "OrbitMulti GB kurang dari " + str(NOTIF_Q_GB) + " GB", description
    )

    if result_day:
        print(result_day)
        description = "\n".join([msisdn for msisdn in result_day])
    else:
        description = "Tidak Ada"
    send_notification_telegram(
        "OrbitMulti DAY kurang dari " + str(NOTIF_Q_DAY) + " Hari", description
    )


def check_selenium_working():
    orbit = Orbit.objects.order_by("updated_at").last()
    current_time = timezone.now()
    delta_time = current_time - orbit.updated_at

    if delta_time.days > 1:
        description = (
            "Pengecheckan Orbit terlambat lebih dari 1 hari! Segera check BackOne Data!"
        )
    else:
        description = "Pengecheckan Orbit Aman"
    send_notification_telegram("Pengecheckan Orbit", description)

    orbit = OrbitMulti.objects.order_by("updated_at").last()
    current_time = timezone.now()
    delta_time = current_time - orbit.updated_at

    if delta_time.days > 1:
        description = "Pengecheckan Orbit Multi terlambat lebih dari 1 hari! Segera check BackOne Data!"
    else:
        description = "Pengecheckan Orbit Multi Aman"
    send_notification_telegram("Pengecheckan Orbit", description)


def orbit_stat_worker():
    """Start every midnite"""

    orbits = Orbit.objects.all()

    for orbit in orbits:
        quota_string = ""
        msisdn = re.sub("^0", "", orbit.msisdn)
        quota = quota_int(orbit.quota_current)
        quota_string += orbit.quota_current if orbit.quota_current else ""
        quota_string += "/" + orbit.quota_total if orbit.quota_total else ""
        quota_string += "/" + orbit.quota_day if orbit.quota_day else ""

        OrbitStatQuota.objects.create(
            msisdn=msisdn, quota=quota, quota_string=quota_string
        )
        """ Save Quota Previous Day"""
        orbit.quota_prev = quota_string
        orbit.save()

    orbits = OrbitMulti.objects.all()

    for orbit in orbits:
        quota_string = ""
        msisdn = re.sub("^0", "", orbit.msisdn)
        quota = quota_int(orbit.quota_current)
        quota_string += orbit.quota_current if orbit.quota_current else ""
        quota_string += "/" + orbit.quota_total if orbit.quota_total else ""
        quota_string += "/" + orbit.quota_day if orbit.quota_day else ""

        OrbitStatQuota.objects.create(
            msisdn=msisdn, quota=quota, quota_string=quota_string
        )

        """ Save Quota Previous Day"""
        orbit.quota_prev = quota_string
        orbit.save()
