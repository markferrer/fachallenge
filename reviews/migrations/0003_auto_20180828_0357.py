# Generated by Django 2.1 on 2018-08-28 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20180828_0356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviereview',
            old_name='summary_report',
            new_name='summary_short',
        ),
    ]