# Generated by Django 2.0.6 on 2018-12-07 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remo', '0018_serie'),
    ]

    operations = [
        migrations.AddField(
            model_name='serie',
            name='prof',
            field=models.CharField(default='', max_length=60, verbose_name='Profundidade'),
            preserve_default=False,
        ),
    ]