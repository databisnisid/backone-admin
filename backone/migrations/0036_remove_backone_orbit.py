# Generated by Django 4.0.4 on 2022-11-03 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backone', '0035_backone_ping_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backone',
            name='orbit',
        ),
    ]