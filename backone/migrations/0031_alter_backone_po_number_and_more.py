# Generated by Django 4.0.4 on 2022-06-07 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_po_my_company_povendor_my_company_and_more'),
        ('backone', '0030_alter_backone_service_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backone',
            name='po_number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='project.po', verbose_name='PO dari Pelanggan'),
        ),
        migrations.AlterField(
            model_name='backone',
            name='po_number_vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='project.povendor', verbose_name='PO ke Vendor'),
        ),
    ]
