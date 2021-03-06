# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-09 11:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import ojs.models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0023_auto_20170122_0525'),
        ('ojs', '0002_auto_20170123_0458'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmissionRevision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.PositiveIntegerField(default=0)),
                ('file_object', models.FileField(upload_to=ojs.models.submission_filename)),
                ('document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='document.Document')),
            ],
        ),
        migrations.RenameField(
            model_name='submission',
            old_name='submission_id',
            new_name='ojs_identifier',
        ),
        migrations.RenameField(
            model_name='submission',
            old_name='user',
            new_name='submitter',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='document',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='version_id',
        ),
        migrations.AddField(
            model_name='submissionrevision',
            name='submission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ojs.Submission'),
        ),
        migrations.AlterUniqueTogether(
            name='submissionrevision',
            unique_together=set([('version', 'submission')]),
        ),
    ]
