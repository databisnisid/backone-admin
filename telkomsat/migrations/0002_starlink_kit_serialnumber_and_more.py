# Generated by Django 4.2.15 on 2024-09-06 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telkomsat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='starlink',
            name='kit_serialnumber',
            field=models.CharField(blank=True, max_length=50, verbose_name='KIT Serial Number'),
        ),
        migrations.AlterField(
            model_name='starlink',
            name='service_line_number',
            field=models.CharField(max_length=50, unique=True, verbose_name='Service Line Number'),
        ),
    ]
