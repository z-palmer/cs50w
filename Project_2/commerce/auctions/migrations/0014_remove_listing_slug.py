# Generated by Django 4.1.6 on 2023-05-03 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_alter_listing_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='slug',
        ),
    ]
