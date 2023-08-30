# Generated by Django 4.0.4 on 2022-05-29 13:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Baso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('upload_file', models.FileField(upload_to='baso')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'baso',
                'db_table': 'baso',
                'managed': True,
            },
        ),
    ]
