from .models import BackOne
from ipaddress import ip_address
from connector.drivers import ping

PING_PACKET = 1
PING_TIMEOUT = 3
IP_NULL = '0.0.0.0'


def validate_ip_address(address):
    try:
        ip = ip_address(address)
        return True
    except ValueError:
        return False


def update_sites_ping_status():
    location = BackOne.objects.all()
    for loc in location:
        loc.ping_status = False

        if validate_ip_address(loc.ipaddress) and loc.ipaddress != IP_NULL:
            ping_result = ping.ping(loc.ipaddress, PING_PACKET, PING_TIMEOUT)
            loc.ping_status = ping_result
            print('PING', loc.ipaddress, ping_result)

        loc.save()
