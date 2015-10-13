# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('sku', models.CharField(max_length=30)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=50)),
            ],
        ),
    ]
