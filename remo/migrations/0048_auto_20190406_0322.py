# Generated by Django 2.1.7 on 2019-04-06 03:22

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('remo', '0047_auto_20190405_2223'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Serie',
            new_name='Campanha',
        ),
    ]
