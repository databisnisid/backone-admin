# Generated by Django 4.0.4 on 2022-05-27 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
        ('backone', '0014_remove_backone_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='backone',
            name='service_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='service.servicetype'),
        ),
    ]
