from django.db import models
from orbit.models import Orbit


class BackOne(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    ipaddress = models.GenericIPAddressField(default='0.0.0.0')
    serial_number = models.CharField(max_length=30, default='000000000')
    username = models.CharField(max_length=20, default='root')
    password = models.CharField(max_length=20, default='K0l0r1j0')
    location = models.CharField(max_length=50, blank=True, default='-6.202509554265462, 106.81914451645058')
    backone_network = models.CharField(max_length=50, blank=True)
    orbit = models.OneToOneField(
        Orbit,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        managed = True
        db_table = 'backone'
        verbose_name_plural = 'backones'

    def __str__(self):
        return '%s' % self.name

