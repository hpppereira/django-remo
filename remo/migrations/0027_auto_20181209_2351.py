# Generated by Django 2.1.2 on 2018-12-10 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remo', '0026_auto_20181209_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados',
            name='date',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Data'),
        ),
    ]
