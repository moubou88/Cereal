# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cereal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NutritionalFacts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=3, null=True)),
                ('calories', models.IntegerField(null=True)),
                ('protein_g', models.IntegerField(null=True)),
                ('fat', models.IntegerField(null=True)),
                ('sodium', models.IntegerField(null=True)),
                ('dietary_fiber', models.IntegerField(null=True)),
                ('carbs', models.IntegerField(null=True)),
                ('sugars', models.IntegerField(null=True)),
                ('display_shelf', models.IntegerField(null=True)),
                ('potassium', models.IntegerField(null=True)),
                ('vitamins', models.IntegerField(null=True)),
                ('minerals', models.IntegerField(null=True)),
                ('serving_size_weight', models.IntegerField(null=True)),
                ('cups_per_serving', models.FloatField(null=True)),
                ('cereal', models.OneToOneField(to='main.Cereal')),
                ('manufacturer', models.ForeignKey(to='main.Manufacturer', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='cereal',
            name='manufacturer',
            field=models.ForeignKey(to='main.Manufacturer', null=True),
        ),
    ]
