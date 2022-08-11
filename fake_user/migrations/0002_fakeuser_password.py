# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fake_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fakeuser',
            name='password',
            field=models.CharField(verbose_name='password', max_length=128, default='teste'),
            preserve_default=False,
        ),
    ]
