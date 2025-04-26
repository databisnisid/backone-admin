from django.core.management import call_command
from orbit.cron import (
    CRON_get_all_quota_orbit,
    CRON_check_quota_orbit_notification_daily,
)
from orbit.utils import get_all_quota_orbit, get_all_quota_orbit_multi
from dsc.utils import get_quota as dsc_gq

from dsc.utils import get_quota_proit as dscproit_gq
from telkomsat.utils import get_quota as starlink_gq
from time import sleep


def dbbackup_job():
    try:
        call_command("dbbackup")

    except:
        pass


def get_all_quota_dsc():
    # DSC
    dsc_gq()
    sleep(300)
    dscproit_gq()


def get_all_quota_orbit_single():
    get_all_quota_orbit()


def get_telkomsat_quota():
    starlink_gq()


def get_all_quota():
    # Telkomsat
    # starlink_gq()
    # sleep(30)
    get_all_quota_orbit_multi()
    # DSC
    # dsc_gq()
    # sleep(60)
    # DSC Proit
    # dscproit_gq()
    # sleep(60)
    # Orbit
    # CRON_get_all_quota_orbit()
