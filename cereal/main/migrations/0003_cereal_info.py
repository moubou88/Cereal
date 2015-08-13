# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150812_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='cereal',
            name='info',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
