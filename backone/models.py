from django.db import models
#from django.core.exceptions import ValidationError, ObjectDoesNotExist
#from django.utils.translation import gettext as _
from orbit.models import Orbit
from contact.models import Contact
from baso.models import Baso
from django_google_maps import fields as map_fields
from connection.models import ConnectionType, ConnectionStatus
from service.models import ServiceType, ServiceVendor
from project.models import Project, Po, PoVendor


class BackOne(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Nama Site')
    ipaddress = models.GenericIPAddressField(default='0.0.0.0', verbose_name='IP Address')
    ipaddress_local = models.GenericIPAddressField(default='0.0.0.0', verbose_name='IP Address Lokal')
    serial_number = models.CharField(max_length=30, default='000000000', verbose_name='Serial Number')
    sid = models.CharField(max_length=20, default='000000000', verbose_name='SID')
    description = models.TextField(blank=True, verbose_name='Catatan')
    address = map_fields.AddressField(max_length=200, blank=True, verbose_name='Alamat')
    geolocation = map_fields.GeoLocationField(max_length=100, blank=True)
    username = models.CharField(max_length=20, default='root')
    password = models.CharField(max_length=20, default='K0l0r1j0')
    backone_id = models.CharField(max_length=50, blank=True, verbose_name='SDWAN ID Site')
    backone_network = models.CharField(max_length=50, blank=True, verbose_name='SDWAN ID Network')

    orbit = models.OneToOneField(
        Orbit,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        verbose_name='Koneksi Orbit'
    )
    contact = models.ForeignKey(
        Contact,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        verbose_name='Kontak di Site'
    )
    connection_type = models.ForeignKey(
        ConnectionType,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        verbose_name='Jenis Koneksi'
    )
    connection_status = models.ForeignKey(
        ConnectionStatus,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        verbose_name='Status Koneksi'
    )
    service_type = models.ForeignKey(
        ServiceType,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        verbose_name='Layanan Yang Dijual'
    )
    service_vendor = models.ForeignKey(
        ServiceVendor,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        verbose_name='Layanan Yang Dibeli'
    )
    po_number = models.ForeignKey(
        Po,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        verbose_name='PO dari Pelanggan'
    )
    po_number_vendor = models.ForeignKey(
        PoVendor,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        verbose_name='PO ke Vendor'
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        verbose_name='Nama Project'
    )
    baso = models.ForeignKey(
        Baso,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        verbose_name='Nomor BASO'
    )
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        managed = True
        db_table = 'backone'
        verbose_name = 'site'
        verbose_name_plural = 'Daftar Sites'

    def __str__(self):
        return '%s' % self.name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        return super(BackOne, self).save(*args, **kwargs)
