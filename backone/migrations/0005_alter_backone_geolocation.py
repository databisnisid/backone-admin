# Generated by Django 4.0.4 on 2022-05-24 17:42

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backone', '0004_backone_address_backone_geolocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backone',
            name='geolocation',
            field=django_google_maps.fields.GeoLocationField(default='-6.202509554265462, 106.81914451645058', max_length=100),
        ),
    ]
