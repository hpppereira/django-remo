# Generated by Django 2.0.7 on 2018-10-28 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remo', '0007_auto_20181011_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_en',
            field=models.CharField(max_length=200, verbose_name='Titulo em Inglês'),
        ),
    ]