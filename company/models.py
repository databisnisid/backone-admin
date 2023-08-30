from django.db import models
from django_google_maps import fields as map_fields


class MyCompany(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nama PT')
    code = models.CharField(max_length=10, unique=True, verbose_name='Singkatan Nama PT')
    address = map_fields.AddressField(max_length=200, blank=True, verbose_name='Alamat')
    geolocation = map_fields.GeoLocationField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        managed = True
        db_table = 'my_company'
        verbose_name = 'Daftar PT Kita'
        verbose_name_plural = 'Daftar PT Kita'

    def __str__(self):
        return '%s (%s)' % (self.name, self.code)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.code = self.code.upper()
        return super(MyCompany, self).save(*args, **kwargs)


class OtherCompany(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nama PT')
    code = models.CharField(max_length=10, unique=True, verbose_name='Singkatan Nama PT')
    address = map_fields.AddressField(max_length=200, blank=True, verbose_name='Alamat')
    geolocation = map_fields.GeoLocationField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        managed = True
        db_table = 'other_company'
        verbose_name = 'Daftar PT Client/Vendor'
        verbose_name_plural = 'Daftar PT Client/Vendor'

    def __str__(self):
        return '%s (%s)' % (self.name, self.code)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.code = self.code.upper()
        return super(OtherCompany, self).save(*args, **kwargs)

