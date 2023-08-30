from orbit.cron import CRON_check_quota_orbit_notification_daily
from statistic.utils import send_report_connection_status


def CRON_daily_report():
    CRON_check_quota_orbit_notification_daily()
    send_report_connection_status()
