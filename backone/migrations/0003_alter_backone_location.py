# Generated by Django 4.0.4 on 2022-05-22 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backone', '0002_alter_backone_options_backone_serial_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backone',
            name='location',
            field=models.CharField(blank=True, default='-6.202509554265462, 106.81914451645058', max_length=50),
        ),
    ]
