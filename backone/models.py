from django.db import models
from orbit.models import Orbit
from contact.models import Contact
from django_google_maps import fields as map_fields
from connection.models import ConnectionType, ConnectionStatus
from service.models import ServiceType, ServiceVendor
#from django.db.models import UniqueConstraint
#from django.db.models.functions import Lower


class BackOne(models.Model):
    name = models.CharField(max_length=50, unique=True)
    ipaddress = models.GenericIPAddressField(default='0.0.0.0')
    serial_number = models.CharField(max_length=30, default='000000000')
    sid = models.CharField(max_length=20, default='000000000')
    description = models.TextField(blank=True)
    address = map_fields.AddressField(max_length=200, blank=True)
    geolocation = map_fields.GeoLocationField(max_length=100, blank=True)
    username = models.CharField(max_length=20, default='root')
    password = models.CharField(max_length=20, default='K0l0r1j0')
    backone_network = models.CharField(max_length=50, blank=True)

    orbit = models.OneToOneField(
        Orbit,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    contact = models.ForeignKey(
        Contact,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    connection_type = models.ForeignKey(
        ConnectionType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    connection_status = models.ForeignKey(
        ConnectionStatus,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    service_type = models.ForeignKey(
        ServiceType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    service_vendor = models.ForeignKey(
        ServiceVendor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        managed = True
        db_table = 'backone'
        verbose_name = 'site'
        verbose_name_plural = 'sites'

    def __str__(self):
        return '%s' % self.name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        return super(BackOne, self).save(*args, **kwargs)

