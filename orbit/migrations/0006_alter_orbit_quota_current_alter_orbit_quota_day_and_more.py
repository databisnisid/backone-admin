# Generated by Django 4.0.4 on 2022-06-09 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orbit', '0005_alter_orbit_imei_alter_orbit_msisdn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orbit',
            name='quota_current',
            field=models.CharField(blank=True, max_length=20, verbose_name='Kuota Saat Ini'),
        ),
        migrations.AlterField(
            model_name='orbit',
            name='quota_day',
            field=models.CharField(blank=True, max_length=20, verbose_name='Kuota Hari'),
        ),
        migrations.AlterField(
            model_name='orbit',
            name='quota_total',
            field=models.CharField(blank=True, max_length=20, verbose_name='Kuota Total'),
        ),
    ]
