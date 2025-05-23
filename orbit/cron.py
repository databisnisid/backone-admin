from time import sleep
from .utils import (
    get_all_quota_orbit,
    check_quota_orbit_notification_daily,
    get_all_quota_orbit_multi,
    check_quota_orbit_multi_notification_daily,
    check_selenium_working,
)


def CRON_get_all_quota_orbit():
    get_all_quota_orbit_multi()
    sleep(300)
    get_all_quota_orbit()


def CRON_check_quota_orbit_notification_daily():
    check_quota_orbit_notification_daily()
    check_quota_orbit_multi_notification_daily()
    check_selenium_working()
