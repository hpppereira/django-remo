# Generated by Django 2.1.2 on 2018-12-10 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('remo', '0020_auto_20181207_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='dados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Data')),
                ('ate', models.FloatField(blank=True, null=True, verbose_name='ate')),
                ('bat', models.FloatField(blank=True, null=True, verbose_name='bat')),
                ('bp', models.FloatField(blank=True, null=True, verbose_name='bp')),
                ('con', models.FloatField(blank=True, null=True, verbose_name='con')),
                ('dir1', models.FloatField(blank=True, null=True, verbose_name='dir1')),
                ('dir2', models.FloatField(blank=True, null=True, verbose_name='dir2')),
                ('dir3', models.FloatField(blank=True, null=True, verbose_name='dir3')),
                ('dp', models.FloatField(blank=True, null=True, verbose_name='dp')),
                ('hs', models.FloatField(blank=True, null=True, verbose_name='hs')),
                ('lat', models.FloatField(blank=True, null=True, verbose_name='lat')),
                ('lon', models.FloatField(blank=True, null=True, verbose_name='lon')),
                ('mag1', models.FloatField(blank=True, null=True, verbose_name='mag1')),
                ('mag2', models.FloatField(blank=True, null=True, verbose_name='mag2')),
                ('mag3', models.FloatField(blank=True, null=True, verbose_name='mag3')),
                ('psbe10', models.FloatField(blank=True, null=True, verbose_name='psbe10')),
                ('psbe100', models.FloatField(blank=True, null=True, verbose_name='psbe100')),
                ('rh', models.FloatField(blank=True, null=True, verbose_name='rh')),
                ('tdl', models.FloatField(blank=True, null=True, verbose_name='tdl')),
                ('tp', models.FloatField(blank=True, null=True, verbose_name='tp')),
                ('tsbe10', models.FloatField(blank=True, null=True, verbose_name='tsbe10')),
                ('tsbe100', models.FloatField(blank=True, null=True, verbose_name='tsbe100')),
                ('tsbe20', models.FloatField(blank=True, null=True, verbose_name='tsbe20')),
                ('tsbe30', models.FloatField(blank=True, null=True, verbose_name='tsbe30')),
                ('tsbe40', models.FloatField(blank=True, null=True, verbose_name='tsbe40')),
                ('tsbe50', models.FloatField(blank=True, null=True, verbose_name='tsbe50')),
                ('tsbe60', models.FloatField(blank=True, null=True, verbose_name='tsbe60')),
                ('tsbe70', models.FloatField(blank=True, null=True, verbose_name='tsbe70')),
                ('tsbe80', models.FloatField(blank=True, null=True, verbose_name='tsbe80')),
                ('tsbe90', models.FloatField(blank=True, null=True, verbose_name='tsbe90')),
                ('tsup', models.FloatField(blank=True, null=True, verbose_name='tsup')),
                ('wd', models.FloatField(blank=True, null=True, verbose_name='wd')),
                ('ws', models.FloatField(blank=True, null=True, verbose_name='ws')),
                ('campanha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remo.Serie', verbose_name='Estação')),
            ],
            options={
                'verbose_name': 'Dados de Campanhas',
                'verbose_name_plural': 'Dados de Campanhas',
            },
        ),
    ]