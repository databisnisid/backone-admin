# Generated by Django 4.0.4 on 2022-06-08 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backone', '0031_alter_backone_po_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='backone',
            name='is_priority',
            field=models.BooleanField(default=False, verbose_name='Priority Site'),
        ),
    ]
