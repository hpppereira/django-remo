# Generated by Django 2.0.6 on 2019-02-08 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remo', '0036_auto_20181230_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='destaque',
            name='url',
            field=models.CharField(default='', max_length=200, verbose_name='URL'),
            preserve_default=False,
        ),
    ]
