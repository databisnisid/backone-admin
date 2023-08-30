from slick_reporting.views import SlickReportView
from slick_reporting.fields import SlickReportField
from slick_reporting.decorators import report_field_register
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BackOne
from django.shortcuts import render
from orbit.models import Orbit
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.db.models import Count


class SiteReport(LoginRequiredMixin, SlickReportView):
    # The model where you have the data
    report_model = BackOne

    # the main date field used for the model.
    date_field = 'created_at' # or 'order__date_placed'
    # this support traversing, like so
    # date_field = 'order__date_placed'

    # A foreign key to group calculation on
    #group_by = 'project'

    #limit_records = 25
    # The columns you want to display
    columns = ['name', 'connection_status__name', 'service_type__name', 'baso__date',
            #SlickReportField.create(method=Count, field='project', name='project', verbose_name='Total Project')
            ]
    # Charts
    """
    charts_settings = [
     {
        'type': 'bar',
        'data_source': 'project',
        'title_source': 'name',
     },
    ]
    """


def get_quota_current(request, ipaddress=None):
    q_current = 0
    try:
        backone = BackOne.objects.get(ipaddress=ipaddress)
        is_found = True if backone.orbit else False

    except ObjectDoesNotExist:
        is_found = False

    if is_found:
        orbit = Orbit.objects.get(id=backone.orbit.id)
        q_current_string = orbit.quota_current.split()
        q_current = float(q_current_string[0])

    return HttpResponse(q_current)


def get_quota_day(request, ipaddress=None):
    q_day = 0
    try:
        backone = BackOne.objects.get(ipaddress=ipaddress)
        is_found = True if backone.orbit else False

    except ObjectDoesNotExist:
        is_found = False

    if is_found:
        orbit = Orbit.objects.get(id=backone.orbit.id)
        q_day_string = orbit.quota_day.split()
        q_day = float(q_day_string[0])

    return HttpResponse(q_day)
