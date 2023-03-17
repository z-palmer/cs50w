# Generated by Django 4.1.6 on 2023-03-16 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cash',
            field=models.PositiveIntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('time_left', models.DurationField()),
                ('posting', models.DateTimeField()),
                ('image', models.ImageField(upload_to='')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listing', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('content', models.TextField(max_length=500)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('amount', models.CharField(max_length=64)),
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('listing_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bid', to='auctions.listing')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bid', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]