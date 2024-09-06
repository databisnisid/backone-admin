from django.db import models
from backone.models import BackOne
from django.utils.translation import gettext_lazy as _
from datetime import datetime

class Starlink(models.Model):
    service_line_number = models.CharField(max_length=50, verbose_name=_('Service Line Number'))
    quota_total = models.CharField(max_length=20, blank=True, verbose_name='Kuota Total', default='40 GB')
    quota_current = models.CharField(max_length=20, blank=True, verbose_name='Kuota Saat Ini')
    quota_usage = models.CharField(max_length=20, blank=True, verbose_name='Kuota Usage')
    quota_until = models.CharField(max_length=20, blank=True, verbose_name='Kuota Masa Berlaku ')
    quota_date = models.DateField(_('Berlaku Sampai'), blank=True, null=True)
    quota_day =models.CharField(_('Kuota Hari'), max_length=20, blank=True, null=True)
    quota_prev = models.CharField(max_length=100, blank=True, null=True, verbose_name='Quota Prev')

    additional_info = models.TextField(blank=True, null=True, verbose_name='Keterangan')


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
        return '%s(%s/%s)' % (self.service_line_number, self.quota_current, self.quota_until)


