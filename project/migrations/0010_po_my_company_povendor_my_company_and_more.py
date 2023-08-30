# Generated by Django 4.0.4 on 2022-06-07 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('project', '0009_remove_povendor_project_povendor_po_base'),
    ]

    operations = [
        migrations.AddField(
            model_name='po',
            name='my_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='company.mycompany', verbose_name='PO untuk PT'),
        ),
        migrations.AddField(
            model_name='povendor',
            name='my_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='company.mycompany', verbose_name='PO menggunakan PT'),
        ),
        migrations.AddField(
            model_name='povendor',
            name='other_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='company.othercompany', verbose_name='PO untuk PT'),
        ),
    ]