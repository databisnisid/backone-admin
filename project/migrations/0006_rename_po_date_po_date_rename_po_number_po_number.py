# Generated by Django 4.0.4 on 2022-05-29 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_po_upload_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='po',
            old_name='po_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='po',
            old_name='po_number',
            new_name='number',
        ),
    ]
