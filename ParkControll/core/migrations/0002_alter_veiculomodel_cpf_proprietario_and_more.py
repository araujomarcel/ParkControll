# Generated by Django 4.1.9 on 2023-05-25 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculomodel',
            name='cpf_proprietario',
            field=models.IntegerField(verbose_name='cpf_proprietario'),
        ),
        migrations.AlterField(
            model_name='veiculomodel',
            name='telefone',
            field=models.IntegerField(verbose_name='telefone'),
        ),
    ]
