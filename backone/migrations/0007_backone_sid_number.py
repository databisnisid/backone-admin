# Generated by Django 4.0.4 on 2022-05-25 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backone', '0006_alter_backone_geolocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='backone',
            name='sid_number',
            field=models.CharField(default='000000000', max_length=20),
        ),
    ]