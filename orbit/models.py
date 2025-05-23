from django.db import models
from backone.models import BackOne


class Orbit(models.Model):
    username = models.EmailField(max_length=50, default="nopass@backone.cloud")
    password = models.CharField(max_length=50, default="nopassword")
    msisdn = models.CharField(max_length=30, verbose_name="MSISDN")
    imei = models.CharField(max_length=30, verbose_name="IMEI")
    quota_total = models.CharField(
        max_length=20, blank=True, verbose_name="Kuota Total"
    )
    quota_current = models.CharField(
        max_length=20, blank=True, verbose_name="Kuota Saat Ini"
    )
    quota_day = models.CharField(max_length=200, blank=True, verbose_name="Kuota Hari")
    quota_prev = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Quota Prev"
    )
    quota_type = models.CharField(
        max_length=20, default="orbit", verbose_name="Quota Type"
    )
    error_msg = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Error Message"
    )

    additional_info = models.TextField(blank=True, null=True, verbose_name="Keterangan")

    site = models.OneToOneField(
        BackOne, on_delete=models.RESTRICT, null=True, blank=True, verbose_name="Site"
    )

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        managed = True
        db_table = "orbit"
        verbose_name_plural = "Daftar Orbit"

    def __str__(self):
        return "%s(%s/%s-%s)" % (
            self.imei,
            self.quota_current,
            self.quota_total,
            self.quota_day,
        )


class OrbitMulti(models.Model):
    username = models.EmailField(max_length=50, default="nopass@backone.cloud")
    password = models.CharField(max_length=50, default="nopassword")
    msisdn = models.CharField(
        max_length=30, verbose_name="MSISDN", blank=True, null=True
    )
    imei = models.CharField(max_length=30, verbose_name="IMEI", blank=True, null=True)
    quota_total = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Kuota Total"
    )
    quota_current = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Kuota Saat Ini"
    )
    quota_day = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Kuota Hari"
    )
    quota_prev = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Quota Prev"
    )
    quota_type = models.CharField(
        max_length=20, default="orbit", verbose_name="Quota Type"
    )

    additional_info = models.TextField(blank=True, null=True, verbose_name="Keterangan")

    site = models.OneToOneField(
        BackOne, on_delete=models.RESTRICT, null=True, blank=True, verbose_name="Site"
    )

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        managed = True
        db_table = "orbit_multi"
        verbose_name_plural = "Daftar Orbit Multi"

    def __str__(self):
        return "%s(%s/%s-%s)" % (
            self.imei,
            self.quota_current,
            self.quota_total,
            self.quota_day,
        )


class OrbitStatQuota(models.Model):
    msisdn = models.CharField(max_length=30, verbose_name="MSISDN")
    quota = models.IntegerField()
    quota_string = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        managed = True
        db_table = "orbit_stat"
        verbose_name = "Orbit Statistic"
        verbose_name_plural = "Orbit Statistics"

    def __str__(self):
        return "{}".format(self.msisdn)
