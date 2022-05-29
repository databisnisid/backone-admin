from django.db import models
from django.utils import timezone


class Project(models.Model):
    name = models.CharField(max_length=50, unique=True)
    contact_name = models.CharField(max_length=50, blank=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        managed = True
        db_table = 'project'
        verbose_name_plural = 'projects'

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
    )
    number = models.CharField(max_length=50, unique=True)
    date = models.DateField(default=timezone.now)
    upload_file = models.FileField(upload_to='po', blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        managed = True
        db_table = 'po'
        verbose_name = 'purchase order'
        verbose_name_plural = 'purchase orders'

    def __str__(self):
        return '%s (%s)' % (self.number, self.project)

    def save(self, *args, **kwargs):
        self.number = self.number.upper()
        return super(Po, self).save(*args, **kwargs)
