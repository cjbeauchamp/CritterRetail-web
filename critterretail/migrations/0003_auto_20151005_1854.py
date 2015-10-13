# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('critterretail', '0002_product_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.AddField(
            model_name='productreview',
            name='product',
            field=models.ForeignKey(to='critterretail.Product'),
        ),
        migrations.AddField(
            model_name='productrating',
            name='product',
            field=models.ForeignKey(to='critterretail.Product'),
        ),
    ]
