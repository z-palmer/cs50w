# Generated by Django 4.1.6 on 2023-04-23 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_listing_comments_alter_listing_current_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='slug',
            field=models.SlugField(default='', max_length=250, unique_for_date='posting'),
            preserve_default=False,
        ),
    ]