# Generated by Django 2.0.6 on 2019-05-01 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remo', '0049_auto_20190406_0351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo em Português')),
                ('title_en', models.CharField(max_length=200, verbose_name='Titulo em Inglês')),
                ('docs', models.FileField(blank=True, null=True, upload_to='docs/', verbose_name='Imagem')),
                ('url', models.CharField(max_length=200, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
            },
        ),
        migrations.AlterField(
            model_name='publicacao',
            name='ano',
            field=models.CharField(blank=True, default='#', max_length=4, null=True, verbose_name='Ano'),
        ),
        migrations.AlterField(
            model_name='publicacao',
            name='authors',
            field=models.CharField(blank=True, default='#', max_length=200, null=True, verbose_name='Autores'),
        ),
        migrations.AlterField(
            model_name='publicacao',
            name='title',
            field=models.CharField(blank=True, default='#', max_length=200, null=True, verbose_name='Titulo'),
        ),
    ]
