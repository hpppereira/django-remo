# Generated by Django 2.1.2 on 2018-11-28 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remo', '0016_auto_20181128_0014'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='destaque',
            options={'verbose_name': 'Destaques', 'verbose_name_plural': 'Destaques'},
        ),
        migrations.AlterModelOptions(
            name='doc',
            options={'verbose_name': 'Documentos', 'verbose_name_plural': 'Documentos'},
        ),
        migrations.AlterModelOptions(
            name='doi',
            options={'verbose_name': 'DOI', 'verbose_name_plural': 'DOI'},
        ),
        migrations.AlterModelOptions(
            name='estacao',
            options={'verbose_name': 'Estações', 'verbose_name_plural': 'Estações'},
        ),
        migrations.AlterModelOptions(
            name='index',
            options={'verbose_name': 'Index', 'verbose_name_plural': 'Index'},
        ),
        migrations.AlterModelOptions(
            name='institution',
            options={'verbose_name': 'Instituições Parceiras', 'verbose_name_plural': 'Instituições Parceiras'},
        ),
        migrations.AlterModelOptions(
            name='noticia',
            options={'verbose_name': 'Notícias', 'verbose_name_plural': 'Notícias'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Colaborador', 'verbose_name_plural': 'Colaborador'},
        ),
        migrations.AlterModelOptions(
            name='publicacao',
            options={'verbose_name': 'Publicações', 'verbose_name_plural': 'Publicações'},
        ),
        migrations.AddField(
            model_name='institution',
            name='estado',
            field=models.CharField(default='', max_length=2, verbose_name='UF'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='destaque',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='imagens/', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='imagens/', verbose_name='Documento'),
        ),
        migrations.AlterField(
            model_name='doi',
            name='doi',
            field=models.CharField(blank=True, help_text='Caso a publicação não tenha DOI, preencher tudo manualmente', max_length=200, null=True, verbose_name='Doi'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='imagens/', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='paginas',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='imagens/', verbose_name='Documento'),
        ),
    ]