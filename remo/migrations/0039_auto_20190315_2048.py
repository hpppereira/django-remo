# Generated by Django 2.1.7 on 2019-03-15 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remo', '0038_auto_20190315_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='csv',
            field=models.FileField(blank=True, null=True, upload_to='data/', verbose_name='csv'),
        ),
    ]