# Generated by Django 2.1.2 on 2018-11-07 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('remo', '0013_institution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remo.Institution'),
        ),
    ]
