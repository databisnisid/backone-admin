import requests
from django.conf import settings


def get_data_usage(serviceLineNumber:str, start:int, end:int) -> dict:
    s = requests.Session()
    s.headers.update({'Authorization': settings.TELKOMSAT_TOKEN})

    request_string = settings.TELKOMSAT_URL + '/api/data-usage?'
    request_string += 'serviceLineNumber=' + serviceLineNumber
    request_string += '&start=' + str(start)
    request_string += '&end=' + str(end)

    response = s.get(request_string)

    #response = s.get(settings.TELKOMSAT_URL + '/api/data-usage?serviceLineNumber=SL-1499694-81459-94&start=1725123600000&end=1725601392623')

    return response.json()

