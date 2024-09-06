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

        quota_usage_float : float = 0.0

        if result['success']:
            for data in result['data']:
                quota_usage_float += float(data['dataUsage'])

            starlink.quota_usage = str(round(quota_usage_float, 2)) + ' GB'
            starlink.save()

        print(quota_usage_float)


