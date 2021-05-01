# Generated by Django 2.1.2 on 2018-12-10 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remo', '0023_auto_20181209_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados',
            name='ate',
            field=models.FloatField(blank=True, null=True, verbose_name='ate'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='bat',
            field=models.FloatField(blank=True, null=True, verbose_name='bat'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='bp',
            field=models.FloatField(blank=True, null=True, verbose_name='bp'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='con',
            field=models.FloatField(blank=True, null=True, verbose_name='con'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='dir1',
            field=models.FloatField(blank=True, null=True, verbose_name='dir1'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='dir2',
            field=models.FloatField(blank=True, null=True, verbose_name='dir2'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='dir3',
            field=models.FloatField(blank=True, null=True, verbose_name='dir3'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='dp',
            field=models.FloatField(blank=True, null=True, verbose_name='dp'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='hs',
            field=models.FloatField(blank=True, null=True, verbose_name='hs'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='lat',
            field=models.FloatField(blank=True, null=True, verbose_name='lat'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='lon',
            field=models.FloatField(blank=True, null=True, verbose_name='lon'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='mag1',
            field=models.FloatField(blank=True, null=True, verbose_name='mag1'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='mag2',
            field=models.FloatField(blank=True, null=True, verbose_name='mag2'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='mag3',
            field=models.FloatField(blank=True, null=True, verbose_name='mag3'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='psbe10',
            field=models.FloatField(blank=True, null=True, verbose_name='psbe10'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='psbe100',
            field=models.FloatField(blank=True, null=True, verbose_name='psbe100'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='rh',
            field=models.FloatField(blank=True, null=True, verbose_name='rh'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='tdl',
            field=models.FloatField(blank=True, null=True, verbose_name='tdl'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='tp',
            field=models.FloatField(blank=True, null=True, verbose_name='tp'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='tsbe10',
            field=models.FloatField(blank=True, null=True, verbose_name='tsbe10'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='tsbe100',
            field=models.FloatField(blank=True, null=True, verbose_name='tsbe100'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='tsbe20',
            field=models.FloatField(blank=True, null=True, verbose_name='tsbe20'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='tsbe30',
            field=models.FloatField(blank=True, null=True, verbose_name='tsbe30'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='tsbe40',
            field=models.FloatField(blank=True, null=True, verbose_name='tsbe40'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='tsbe50',
            field=models.FloatField(blank=True, null=True, verbose_name='tsbe50'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='tsbe60',
            field=models.FloatField(blank=True, null=True, verbose_name='tsbe60'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='tsbe70',
            field=models.FloatField(blank=True, null=True, verbose_name='tsbe70'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='tsbe80',
            field=models.FloatField(blank=True, null=True, verbose_name='tsbe80'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='tsbe90',
            field=models.FloatField(blank=True, null=True, verbose_name='tsbe90'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='tsup',
            field=models.FloatField(blank=True, null=True, verbose_name='tsup'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='wd',
            field=models.FloatField(blank=True, null=True, verbose_name='wd'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='ws',
            field=models.FloatField(blank=True, null=True, verbose_name='ws'),
        ),
    ]