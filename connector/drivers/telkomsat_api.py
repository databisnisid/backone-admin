import requests
from django.conf import settings


def get_data_usage() -> dict:
    s = requests.Session()
    s.headers.update({'Authorization': settings.TELKOMSAT_TOKEN})

    response = s.get('https://starmon1.telkomsat.co.id/api/data-usage?serviceLineNumber=SL-1499694-81459-94&start=1725123600000&end=1725601392623')

    return response.json()

