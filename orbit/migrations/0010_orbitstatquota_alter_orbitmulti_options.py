# Generated by Django 4.0.4 on 2023-10-14 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orbit', '0009_orbitmulti'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrbitStatQuota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msisdn', models.CharField(max_length=30, verbose_name='MSISDN')),
                ('quota', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Orbit Statistic',
                'verbose_name_plural': 'Orbit Statistics',
                'db_table': 'orbit_stat',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='orbitmulti',
            options={'managed': True, 'verbose_name_plural': 'Daftar Orbit Multi'},
        ),
    ]
