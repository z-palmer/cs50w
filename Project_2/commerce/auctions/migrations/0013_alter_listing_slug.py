# Generated by Django 4.1.6 on 2023-05-02 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_remove_user_listings_listing_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='slug',
            field=models.SlugField(auto_created=True, max_length=250, unique_for_date=True),
        ),
    ]
