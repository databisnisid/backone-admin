# Generated by Django 4.0.4 on 2022-11-05 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backone', '0036_remove_backone_orbit'),
        ('orbit', '0008_orbit_site'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrbitMulti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.EmailField(default='nopass@backone.cloud', max_length=50)),
                ('password', models.CharField(default='nopassword', max_length=50)),
                ('msisdn', models.CharField(blank=True, max_length=30, null=True, verbose_name='MSISDN')),
                ('imei', models.CharField(blank=True, max_length=30, null=True, verbose_name='IMEI')),
                ('quota_total', models.CharField(blank=True, max_length=20, null=True, verbose_name='Kuota Total')),
                ('quota_current', models.CharField(blank=True, max_length=20, null=True, verbose_name='Kuota Saat Ini')),
                ('quota_day', models.CharField(blank=True, max_length=20, null=True, verbose_name='Kuota Hari')),
                ('additional_info', models.TextField(blank=True, null=True, verbose_name='Keterangan')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('site', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='backone.backone', verbose_name='Site')),
            ],
            options={
                'verbose_name_plural': 'Daftar Orbiti Multi',
                'db_table': 'orbit_multi',
                'managed': True,
            },
        ),
    ]