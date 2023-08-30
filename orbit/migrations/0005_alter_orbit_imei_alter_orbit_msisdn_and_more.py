# Generated by Django 4.0.4 on 2022-06-09 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orbit', '0004_alter_orbit_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orbit',
            name='imei',
            field=models.CharField(max_length=30, verbose_name='IMEI'),
        ),
        migrations.AlterField(
            model_name='orbit',
            name='msisdn',
            field=models.CharField(max_length=30, verbose_name='MSISDN'),
        ),
        migrations.AlterField(
            model_name='orbit',
            name='password',
            field=models.CharField(default='nopassword', max_length=50),
        ),
        migrations.AlterField(
            model_name='orbit',
            name='username',
            field=models.EmailField(default='nopass@backone.cloud', max_length=50),
        ),
    ]