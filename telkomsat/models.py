import calendar
from enum import unique
from django.db import models
from backone.models import BackOne
from django.utils.translation import gettext_lazy as _
from datetime import datetime
#from django.utils.timezone import now
from django.utils import timezone

class Starlink(models.Model):
    #service_line_number = models.CharField(max_length=50, unique=True, verbose_name=_('Service Line Number'))
    msisdn = models.CharField(max_length=50, unique=True, verbose_name=_('Service Line Number'))
    kit_serialnumber = models.CharField(max_length=50, blank=True, verbose_name=_('KIT Serial Number'))
    quota_total = models.CharField(max_length=20, blank=True, verbose_name='Kuota Total', default='40 GB')
    quota_current = models.CharField(max_length=20, blank=True, verbose_name='Kuota Saat Ini')
    quota_usage = models.CharField(max_length=20, blank=True, verbose_name='Kuota Usage')
    quota_until = models.CharField(max_length=20, blank=True, verbose_name='Kuota Masa Berlaku ')
    quota_date = models.DateField(_('Berlaku Sampai'), blank=True, null=True)
    quota_day =models.CharField(_('Kuota Hari'), max_length=20, blank=True, null=True)
    quota_prev = models.CharField(max_length=100, blank=True, null=True, verbose_name='Quota Prev')
    activation_date = models.DateField(verbose_name=_('Tanggal Aktivasi'), blank=True, default=timezone.now())

    additional_info = models.TextField(blank=True, null=True, verbose_name='Keterangan')
    quota_type = models.CharField(max_length=20, default='starlink', verbose_name='Quota Type')


    site = models.OneToOneField(
        BackOne,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        verbose_name='Site'
    )

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        managed = True
        db_table = 'starlink'
        verbose_name = 'Starlink'
        verbose_name_plural = 'Starlinks'

    def __str__(self):
        return '%s(%s/%s)' % (self.msisdn, self.quota_current, self.quota_until)

    def save(self):

        now = timezone.now().replace(tzinfo=None)
        m = calendar.monthrange(now.year, now.month)
        self.quota_date = timezone.datetime(now.year, now.month, m[1])

        delta = self.quota_date - now
        self.quota_day = str(delta.days) + ' Hari'

        if self.quota_usage:
            quota_split = self.quota_usage.split(' ')
            quota_usage = float(quota_split[0])

            quota_split = self.quota_total.split(' ')
            quota_total = float(quota_split[0])
            quota_current = round(quota_total - quota_usage, 2)
            self.quota_current = str(quota_current) + ' GB'


        return super(Starlink, self).save()
