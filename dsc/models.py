from django.db import models
from backone.models import BackOne


class DscDpi(models.Model):
    msisdn = models.CharField(max_length=30, verbose_name='MSISDN')
    imei = models.CharField(max_length=30, verbose_name='IMEI')
    quota_total = models.CharField(max_length=20, blank=True, verbose_name='Kuota Total')
    quota_current = models.CharField(max_length=20, blank=True, verbose_name='Kuota Saat Ini')
    quota_day = models.CharField(max_length=20, blank=True, verbose_name='Kuota Hari')
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
        db_table = 'dscdpi'
        verbose_name_plural = 'Daftar DPI'

    def __str__(self):
        return '%s(%s/%s-%s)' % (self.msisdn, self.quota_current, self.quota_total, self.quota_day)


class DscDpiStatQuota(models.Model):
    msisdn = models.CharField(max_length=30, verbose_name='MSISDN')
    quota = models.IntegerField()
    quota_string = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'dscdpi_stat'
        verbose_name = 'DPI Statistic'
        verbose_name_plural = 'DPI Statistics'

    def __str__(self):
        return '{}'.format(self.msisdn)

