# Generated by Django 2.0.6 on 2018-06-03 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180603_0138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='countrequest',
            old_name='source_file_name',
            new_name='source_filename',
        ),
    ]