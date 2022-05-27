from django.db import models
from djmoney.models.fields import MoneyField


class ServiceType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = MoneyField(max_digits=19, decimal_places=2, null=True, default_currency='IDR')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        managed = True
        db_table = 'service_type'
        verbose_name_plural = 'service type'

    def __str__(self):
        return '%s' % self.name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        return super(ServiceType, self).save(*args, **kwargs)