# Generated by Django 2.0.6 on 2018-11-14 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remo', '0014_auto_20181107_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='doi',
            name='journal',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Revista'),
        ),
    ]