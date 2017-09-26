# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-18 23:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataEHoraDeInicio', models.DateTimeField(blank=True, null=True)),
                ('nome', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=10)),
                ('uf', models.CharField(max_length=2)),
                ('cidade', models.CharField(max_length=20)),
                ('quadra', models.TextField(blank=True, null=True)),
                ('rua', models.TextField(null=True)),
                ('numero', models.CharField(max_length=6, null=True)),
                ('complemento', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=256)),
                ('telefone', models.CharField(max_length=20)),
                ('idade', models.CharField(max_length=11)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.Endereco')),
            ],
        ),
        migrations.AddField(
            model_name='agenda',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.Usuario'),
        ),
    ]
