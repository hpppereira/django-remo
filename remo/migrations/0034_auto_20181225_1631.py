# Generated by Django 2.1.2 on 2018-12-25 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remo', '0033_auto_20181220_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doi',
            name='doi',
            field=models.CharField(blank=True, help_text='Caso a publicação não tenha DOI, preencher tudo manualmente', max_length=200, null=True, unique=True, verbose_name='Doi'),
        ),
    ]