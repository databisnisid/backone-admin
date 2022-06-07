from django.db import models
from django.utils import timezone


class Baso(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField(default=timezone.now)
    upload_file = models.FileField(upload_to='baso', blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        managed = True
        db_table = 'baso'
        verbose_name_plural = 'Daftar Baso'

    def __str__(self):
        return '%s' % self.name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        return super(Baso, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.upload_file.delete()
        return super(Baso, self).delete(*args, **kwargs)
