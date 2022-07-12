from .models import BackOne
from connector.drivers import ping

PING_PACKET = 1
PING_TIMEOUT = 3


def update_sites_ping_status():
    location = BackOne.objects.all()
    for loc in location:
        if loc.ipaddress is not '0.0.0.0':
            ping_result = ping.ping(loc.ipaddress, PING_PACKET, PING_TIMEOUT)
            loc.ping_status = ping_result
            print('PING', loc.ipaddress, ping_result)
            loc.save()
