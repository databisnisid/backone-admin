# Generated by Django 4.0.4 on 2023-10-15 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orbit', '0011_orbitstatquota_quota_string'),
    ]

    operations = [
        migrations.AddField(
            model_name='orbit',
            name='quota_prev',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Quota Prev'),
        ),
        migrations.AddField(
            model_name='orbitmulti',
            name='quota_prev',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Quota Prev'),
        ),
    ]
