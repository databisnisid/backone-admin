# Generated by Django 4.0.4 on 2022-06-07 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connection', '0005_alter_connectionstatus_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='connectionstatus',
            options={'managed': True, 'verbose_name_plural': 'Status Koneksi'},
        ),
        migrations.AlterModelOptions(
            name='connectiontype',
            options={'managed': True, 'verbose_name_plural': 'Tipe Koneksi'},
        ),
    ]