# Generated by Django 4.0.4 on 2022-06-07 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_servicevendor_remove_servicetype_cost_installation_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicetype',
            options={'managed': True, 'verbose_name_plural': 'Service Types'},
        ),
        migrations.AlterModelOptions(
            name='servicevendor',
            options={'managed': True, 'verbose_name_plural': 'Service Vendors'},
        ),
    ]
