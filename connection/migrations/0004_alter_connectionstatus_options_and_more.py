# Generated by Django 4.0.4 on 2022-05-26 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connection', '0003_connectionstatus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='connectionstatus',
            options={'managed': True, 'verbose_name_plural': 'connection status'},
        ),
        migrations.AlterModelOptions(
            name='connectiontype',
            options={'managed': True, 'verbose_name_plural': 'connection type'},
        ),
    ]
