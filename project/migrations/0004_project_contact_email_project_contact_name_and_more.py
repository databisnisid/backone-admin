# Generated by Django 4.0.4 on 2022-05-29 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_po_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='project',
            name='contact_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='project',
            name='contact_phone',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]