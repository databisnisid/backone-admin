# Generated by Django 4.2.15 on 2024-09-10 09:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telkomsat', '0004_rename_service_line_number_starlink_msisdn_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='starlink',
            name='quota_type',
            field=models.CharField(default='starlink', max_length=20, verbose_name='Quota Type'),
        ),
        migrations.AlterField(
            model_name='starlink',
            name='activation_date',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 9, 10, 9, 5, 19, 955992, tzinfo=datetime.timezone.utc), verbose_name='Tanggal Aktivasi'),
        ),
    ]
