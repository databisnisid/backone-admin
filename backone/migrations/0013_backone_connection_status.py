# Generated by Django 4.0.4 on 2022-05-26 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('connection', '0004_alter_connectionstatus_options_and_more'),
        ('backone', '0012_alter_backone_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='backone',
            name='connection_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='connection.connectionstatus'),
        ),
    ]