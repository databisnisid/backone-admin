from django.db import models


class ConnectionType(models.Model):
    name = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        managed = True
        db_table = 'connection_type'
        verbose_name_plural = 'Tipe Koneksi'

    def __str__(self):
        return '%s' % self.name

    def save(self, *args, **kwargs):
        self.name = str(self.name).upper()
        return super(ConnectionType, self).save(*args, **kwargs)


class ConnectionStatus(models.Model):
    name = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        managed = True
        db_table = 'connection_status'
        verbose_name_plural = 'Status Koneksi'

    def __str__(self):
        return '%s' % self.name

    def save(self, *args, **kwargs):
        self.name = str(self.name).upper()
        return super(ConnectionStatus, self).save(*args, **kwargs)
