# Generated by Django 4.0.4 on 2022-05-26 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backone', '0011_backone_connection_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='backone',
            options={'managed': True, 'verbose_name': 'site', 'verbose_name_plural': 'sites'},
        ),
    ]
