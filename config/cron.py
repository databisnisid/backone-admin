from django.core.management import call_command
from orbit.cron import (
    CRON_get_all_quota_orbit,
    CRON_check_quota_orbit_notification_daily,
)
from dsc.utils import get_quota as dsc_gq

# from dsc.utils import get_quota_proit as dscproit_gq
from telkomsat.utils import get_quota as starlink_gq
from time import sleep


def dbbackup_job():
    try:
        call_command("dbbackup")

    except:
        pass


def get_all_quota():
    # Orbit
    CRON_get_all_quota_orbit()
    sleep(300)
    # Telkomsat
    starlink_gq()
    sleep(300)
    # DSC
    dsc_gq()
    sleep(300)
    # DSC Proit
    # dscproit_gq()
