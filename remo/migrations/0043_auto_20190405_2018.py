# Generated by Django 2.1.7 on 2019-04-05 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remo', '0042_auto_20190402_1051'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Doi',
        ),
        migrations.DeleteModel(
            name='Paginas',
        ),
        migrations.AddField(
            model_name='publicacao',
            name='doi',
            field=models.CharField(blank=True, help_text='Ex: 10.1007/s10236-017-1113-9. Caso a publicação não tenha DOI, preencher os outros campos manualmente', max_length=200, null=True, unique=True, verbose_name='DOI'),
        ),
        migrations.AddField(
            model_name='publicacao',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='URL'),
        ),
    ]
