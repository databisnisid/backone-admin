from warnings import warn
from django.db import models
from backone.models import BackOne
from django.utils.translation import gettext_lazy as _
from datetime import datetime


class DscDpi(models.Model):
    msisdn = models.CharField(max_length=30, verbose_name="MSISDN", unique=True)
    imei = models.CharField(max_length=30, verbose_name="IMEI", blank=True)
    quota_total = models.CharField(
        max_length=20, blank=True, verbose_name="Kuota Total", default="5 GB"
    )
    quota_current = models.CharField(
        max_length=20, blank=True, verbose_name="Kuota Saat Ini"
    )
    quota_until = models.CharField(
        max_length=20, blank=True, verbose_name="Kuota Masa Berlaku "
    )
    quota_date = models.DateField(_("Berlaku Sampai"), blank=True, null=True)
    quota_day = models.CharField(_("Kuota Hari"), max_length=20, blank=True, null=True)
    quota_prev = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Quota Prev"
    )

    additional_info = models.TextField(blank=True, null=True, verbose_name="Keterangan")
    error_msg = models.CharField(
        _("Error Message"), max_length=100, blank=True, null=True
    )
    quota_type = models.CharField(
        max_length=20, default="dpi", verbose_name="Quota Type"
    )

    site = models.OneToOneField(
        BackOne, on_delete=models.RESTRICT, null=True, blank=True, verbose_name="Site"
    )

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        managed = True
        db_table = "dscdpi"
        verbose_name = "DPI"
        verbose_name_plural = "Daftar DPI"

    def __str__(self):
        return "%s(%s/%s)" % (self.msisdn, self.quota_current, self.quota_until)

    def save(self):
        if self.quota_until != "":
            date_format = "%d/%m/%Y"
            try:
                self.quota_date = datetime.strptime(self.quota_until, date_format)

                delta = self.quota_date - datetime.now()
                self.quota_day = str(delta.days) + " Hari"

            except ValueError:
                pass

        return super(DscDpi, self).save()


"""
class DscDpiProit(models.Model):
    msisdn = models.CharField(max_length=30, verbose_name="MSISDN", unique=True)
    imei = models.CharField(max_length=30, verbose_name="IMEI", blank=True)
    quota_total = models.CharField(
        max_length=20, blank=True, verbose_name="Kuota Total", default="5 GB"
    )
    quota_current = models.CharField(
        max_length=20, blank=True, verbose_name="Kuota Saat Ini"
    )
    quota_until = models.CharField(
        max_length=20, blank=True, verbose_name="Kuota Masa Berlaku "
    )
    quota_date = models.DateField(_("Berlaku Sampai"), blank=True, null=True)
    quota_day = models.CharField(_("Kuota Hari"), max_length=20, blank=True, null=True)
    quota_prev = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Quota Prev"
    )

    additional_info = models.TextField(blank=True, null=True, verbose_name="Keterangan")
    error_msg = models.CharField(
        _("Error Message"), max_length=100, blank=True, null=True
    )
    quota_type = models.CharField(
        max_length=20, default="dpi", verbose_name="Quota Type"
    )

    site = models.OneToOneField(
        BackOne, on_delete=models.RESTRICT, null=True, blank=True, verbose_name="Site"
    )

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        managed = True
        db_table = "dscdpi_proit"
        verbose_name = "DPI Proit"
        verbose_name_plural = "Daftar DPI Proit"

    def __str__(self):
        return "%s(%s/%s)" % (self.msisdn, self.quota_current, self.quota_until)
"""


class DscDpiStatQuota(models.Model):
    msisdn = models.CharField(max_length=30, verbose_name="MSISDN")
    quota = models.IntegerField()
    quota_string = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        managed = True
        db_table = "dscdpi_stat"
        verbose_name = "DPI Statistic"
        verbose_name_plural = "DPI Statistics"

    def __str__(self):
        return "{}".format(self.msisdn)
