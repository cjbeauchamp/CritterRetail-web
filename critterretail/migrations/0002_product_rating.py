# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('critterretail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.DecimalField(default=0.0, max_digits=2, decimal_places=1),
            preserve_default=False,
        ),
    ]
