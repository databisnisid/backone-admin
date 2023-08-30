from django.db import models
from backone.models import BackOne

class Orbit(models.Model):
    username = models.EmailField(max_length=50, default='nopass@backone.cloud')
    password = models.CharField(max_length=50, default='nopassword')
    msisdn = models.CharField(max_length=30, verbose_name='MSISDN')
    imei = models.CharField(max_length=30, verbose_name='IMEI')
    quota_total = models.CharField(max_length=20, blank=True, verbose_name='Kuota Total')
    quota_current = models.CharField(max_length=20, blank=True, verbose_name='Kuota Saat Ini')
    quota_day = models.CharField(max_length=20, blank=True, verbose_name='Kuota Hari')

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
        db_table = 'orbit'
        verbose_name_plural = 'Daftar Orbit'

    def __str__(self):
        return '%s(%s/%s-%s)' % (self.imei, self.quota_current, self.quota_total, self.quota_day)

class OrbitMulti(models.Model):
    username = models.EmailField(max_length=50, default='nopass@backone.cloud')
    password = models.CharField(max_length=50, default='nopassword')
    msisdn = models.CharField(max_length=30, verbose_name='MSISDN', blank=True, null=True)
    imei = models.CharField(max_length=30, verbose_name='IMEI', blank=True, null=True)
    quota_total = models.CharField(max_length=20, blank=True, null=True, verbose_name='Kuota Total')
    quota_current = models.CharField(max_length=20, blank=True, null=True, verbose_name='Kuota Saat Ini')
    quota_day = models.CharField(max_length=20, blank=True, null=True, verbose_name='Kuota Hari')

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
        db_table = 'orbit_multi'
        verbose_name_plural = 'Daftar Orbit Multi'

    def __str__(self):
        return '%s(%s/%s-%s)' % (self.imei, self.quota_current, self.quota_total, self.quota_day)

