# Generated by Django 4.0.4 on 2022-06-08 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_po_my_company_povendor_my_company_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='po',
            name='is_new',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='po',
            name='is_priority',
            field=models.BooleanField(default=False, verbose_name='Prioritas'),
        ),
    ]
