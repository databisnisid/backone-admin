# Generated by Django 4.0.4 on 2024-09-06 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backone', '0036_remove_backone_orbit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Starlink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_line_number', models.CharField(max_length=50, verbose_name='Service Line Number')),
                ('quota_total', models.CharField(blank=True, default='40 GB', max_length=20, verbose_name='Kuota Total')),
                ('quota_current', models.CharField(blank=True, max_length=20, verbose_name='Kuota Saat Ini')),
                ('quota_usage', models.CharField(blank=True, max_length=20, verbose_name='Kuota Usage')),
                ('quota_until', models.CharField(blank=True, max_length=20, verbose_name='Kuota Masa Berlaku ')),
                ('quota_date', models.DateField(blank=True, null=True, verbose_name='Berlaku Sampai')),
                ('quota_day', models.CharField(blank=True, max_length=20, null=True, verbose_name='Kuota Hari')),
                ('quota_prev', models.CharField(blank=True, max_length=100, null=True, verbose_name='Quota Prev')),
                ('additional_info', models.TextField(blank=True, null=True, verbose_name='Keterangan')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('site', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='backone.backone', verbose_name='Site')),
            ],
            options={
                'verbose_name': 'Starlink',
                'verbose_name_plural': 'Starlinks',
                'db_table': 'starlink',
                'managed': True,
            },
        ),
    ]
