# Generated by Django 4.1.6 on 2023-03-17 17:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_bid_id_alter_comment_id_alter_listing_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='posting',
        ),
        migrations.AddField(
            model_name='bid',
            name='posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='comment',
            name='posting',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='listing',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='user',
            name='account_email',
            field=models.EmailField(default='N/A', max_length=64),
        ),
        migrations.AddField(
            model_name='user',
            name='account_name',
            field=models.CharField(default='N/A', max_length=20),
        ),
        migrations.AlterField(
            model_name='bid',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='user',
            name='cash',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
