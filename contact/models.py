from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        managed = True
        db_table = 'contact'
        verbose_name_plural = 'Daftar Kontak'

    def __str__(self):
        return '%s(%s)' % (self.name, self.phone)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        return super(Contact, self).save(*args, **kwargs)
