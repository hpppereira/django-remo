# Generated by Django 2.1.2 on 2018-11-28 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('remo', '0015_doi_journal'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Destaques',
            new_name='Destaque',
        ),
        migrations.RenameModel(
            old_name='Publicacoes',
            new_name='Publicacao',
        ),
    ]