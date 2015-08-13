# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cereal',
            name='image',
            field=models.ImageField(null=True, upload_to=b'cereal'),
        ),
        migrations.AddField(
            model_name='cereal',
            name='type',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
