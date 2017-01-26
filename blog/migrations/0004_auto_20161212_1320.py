# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20161212_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='blog_text',
            new_name='text',
        ),
    ]
