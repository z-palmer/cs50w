# Generated by Django 4.1.6 on 2023-05-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_remove_listing_comments_remove_user_bids_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]
