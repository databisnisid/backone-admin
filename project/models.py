from django.db import models
from django.utils import timezone
from company.models import MyCompany, OtherCompany


class Project(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Nama Project (Unik)')
    contact_name = models.CharField(max_length=50, blank=True, verbose_name='Nama Kontak Project')
    contact_email = models.EmailField(blank=True, verbose_name='Email Kontak')
    contact_phone = models.CharField(max_length=30, blank=True, verbose_name='Telpon/HP Kontak')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        managed = True
        db_table = 'project'
        verbose_name_plural = 'Daftar Project'

    def __str__(self):
        return '%s' % self.name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.contact_name = self.contact_name.upper()
        return super(Project, self).save(*args, **kwargs)


class Po(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.RESTRICT,
        verbose_name='Nama Project'
    )
    my_company = models.ForeignKey(
        MyCompany,
        on_delete=models.RESTRICT,
        verbose_name='PO untuk PT',
        null=True,
        blank=True
    )
    number = models.CharField(max_length=50, unique=True, verbose_name='Nomor PO')
    date = models.DateField(default=timezone.now, verbose_name='Tanggal PO')
    upload_file = models.FileField(upload_to='po', blank=True, verbose_name='Document PO Upload')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        managed = True
        db_table = 'po'
        verbose_name = 'Daftar PO dari Pelanggan'
        verbose_name_plural = 'Daftar PO dari Pelanggan'

    def __str__(self):
        return '%s (%s)' % (self.number, self.project)

    def save(self, *args, **kwargs):
        self.number = self.number.upper()
        return super(Po, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.upload_file.delete()
        return super(Po, self).delete(*args, **kwargs)


class PoVendor(models.Model):
    po_base = models.ForeignKey(
        Po,
        on_delete=models.RESTRICT,
        verbose_name='Landasan PO dari Pelanggan',
        null=True,
        blank=True
    )
    my_company = models.ForeignKey(
        MyCompany,
        on_delete=models.RESTRICT,
        verbose_name='PO menggunakan PT',
        null=True,
        blank=True
    )
    other_company = models.ForeignKey(
        OtherCompany,
        on_delete=models.RESTRICT,
        verbose_name='PO untuk PT',
        null=True,
        blank=True
    )
    number = models.CharField(max_length=50, unique=True, verbose_name='Nomor PO')
    date = models.DateField(default=timezone.now, verbose_name='Tanggal PO')
    upload_file = models.FileField(upload_to='po_vendor', blank=True, verbose_name='Document PO Upload')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        managed = True
        db_table = 'po_vendor'
        verbose_name = 'Daftar PO ke Vendor'
        verbose_name_plural = 'Daftar PO ke Vendor'

    def __str__(self):
        return '%s' % self.number

    def save(self, *args, **kwargs):
        self.number = self.number.upper()
        return super(PoVendor, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.upload_file.delete()
        return super(PoVendor, self).delete(*args, **kwargs)