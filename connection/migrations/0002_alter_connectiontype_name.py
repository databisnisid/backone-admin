# Generated by Django 4.0.4 on 2022-05-26 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectiontype',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]