from .models import DscDpi  # , DscDpiProit
from connector.drivers.dsc import login_to_dsc
from django.conf import settings


def get_quota():

    members = DscDpi.objects.all()
    members_msisdn = members.values_list("msisdn", flat=True)
    msisdns = list(members_msisdn)

    result = login_to_dsc(msisdns)
    print(result)

    if result:
        for msisdn in msisdns:
            member = members.get(msisdn=msisdn)
            member.quota_total = "5 GB"
            quota_current = result[msisdn]["quota_value"]
            if quota_current != "":
                member.quota_prev = member.quota_current
                member.quota_current = quota_current

            quota_date = result[msisdn]["quota_date"]
            if quota_date != "":
                quota_until = quota_date.split(" ")
                member.quota_until = quota_until[1]

            member.error_msg = result[msisdn]["error_msg"]
            # if quota_current != "" and quota_date != "":
            member.save()
            # print("Save:", msisdn)


"""
def get_quota_proit():

    members = DscDpiProit.objects.all()
    members_msisdn = members.values_list("msisdn", flat=True)
    msisdns = list(members_msisdn)

    result = login_to_dsc(
        msisdns,
        settings.DSC_USERNAME_2,
        settings.DSC_PASSWORD_2,
        settings.DSC_EMAIL_ADDRESS_2,
        settings.DSC_EMAIL_PASSWORD_2,
    )
    print(result)

    if result:
        for msisdn in msisdns:
            member = members.get(msisdn=msisdn)
            member.quota_total = "5 GB"
            quota_current = result[msisdn]["quota_value"]
            if quota_current != "":
                member.quota_prev = member.quota_current
                member.quota_current = quota_current

            quota_date = result[msisdn]["quota_date"]
            if quota_date != "":
                quota_until = quota_date.split(" ")
                member.quota_until = quota_until[1]

            member.error_msg = result[msisdn]["error_msg"]
            # if quota_current != "" and quota_date != "":
            member.save()
            # print("Save:", msisdn)
"""
