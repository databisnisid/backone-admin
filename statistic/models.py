from django.db import models


class Statistic(models.Model):
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    cstatus_all = models.IntegerField()
    cstatus_live = models.IntegerField()
    ctype_vpnip = models.IntegerField()
    ctype_sdwan = models.IntegerField()


    class Meta:
        db_table = 'statistic'
        verbose_name_plural = 'Statistics'

    def __str__(self):
        return '%s' % self.timestamp