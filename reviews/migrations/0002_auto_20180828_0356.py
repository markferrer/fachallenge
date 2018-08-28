# Generated by Django 2.1 on 2018-08-28 03:56

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviereview',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='moviereview',
            name='opening_date',
        ),
        migrations.RemoveField(
            model_name='moviereview',
            name='publication_date',
        ),
        migrations.AddField(
            model_name='moviereview',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='moviereview',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True),
        ),
    ]
