# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='Choice_text',
            new_name='choice_text',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='Question',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='Question_text',
            new_name='question_text',
        ),
    ]
