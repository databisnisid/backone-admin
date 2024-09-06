from .models import Starlink
from django.utils import timezone
from connector.drivers.telkomsat_api import get_data_usage


def get_quota():

    starlinks = Starlink.objects.all()

    for starlink in starlinks:
        current_time = timezone.now()
        first_time = timezone.datetime(current_time.year, 
                                       current_time.month, 1)


        ct_epoch = int(current_time.timestamp() * 1000)
        ft_epoch = int(first_time.timestamp() * 1000)

        
        result = get_data_usage(starlink.service_line_number, ft_epoch, ct_epoch)

        print(result)


