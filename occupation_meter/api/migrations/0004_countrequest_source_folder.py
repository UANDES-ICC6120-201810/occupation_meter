# Generated by Django 2.0.6 on 2018-06-08 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180603_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='countrequest',
            name='source_folder',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]