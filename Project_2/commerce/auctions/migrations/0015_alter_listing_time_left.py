# Generated by Django 4.1.6 on 2023-03-21 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_alter_listing_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='time_left',
            field=models.DurationField(default=7),
        ),
    ]
