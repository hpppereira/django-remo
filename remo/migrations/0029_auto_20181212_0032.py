# Generated by Django 2.0.7 on 2018-12-12 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remo', '0028_auto_20181212_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estacao',
            name='infos',
        ),
        migrations.AddField(
            model_name='serie',
            name='infos',
            field=models.TextField(blank=True, null=True, verbose_name='Informações'),
        ),
    ]
