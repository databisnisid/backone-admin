# Generated by Django 4.0.4 on 2022-05-29 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_po_upload_file'),
        ('baso', '0001_initial'),
        ('contact', '0001_initial'),
        ('connection', '0004_alter_connectionstatus_options_and_more'),
        ('service', '0003_servicevendor_remove_servicetype_cost_installation_and_more'),
        ('orbit', '0002_alter_orbit_options'),
        ('backone', '0020_backone_po_number_backone_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='backone',
            name='baso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='baso.baso'),
        ),
        migrations.AlterField(
            model_name='backone',
            name='connection_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='connection.connectionstatus'),
        ),
        migrations.AlterField(
            model_name='backone',
            name='connection_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='connection.connectiontype'),
        ),
        migrations.AlterField(
            model_name='backone',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='contact.contact'),
        ),
        migrations.AlterField(
            model_name='backone',
            name='orbit',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='orbit.orbit'),
        ),
        migrations.AlterField(
            model_name='backone',
            name='po_number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='project.po'),
        ),
        migrations.AlterField(
            model_name='backone',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='project.project'),
        ),
        migrations.AlterField(
            model_name='backone',
            name='service_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='service.servicetype'),
        ),
        migrations.AlterField(
            model_name='backone',
            name='service_vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='service.servicevendor'),
        ),
    ]