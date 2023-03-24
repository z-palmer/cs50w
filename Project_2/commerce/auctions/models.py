from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models
from datetime import timedelta


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    cash = models.DecimalField(max_digits=8, decimal_places=2)
    account_name = models.CharField(max_length=20, default='N/A')
    account_email = models.EmailField(max_length=64, default='N/A')


class Listing(models.Model):

    LISTING_CATEGORIES = [
        ('LC', 'Listing Category'), ('TY', 'Toys'), ('AN',
                                                     'Antiques'), ('ME', 'Memorabilia'),
        ('TO', 'Tools'), ('CA', 'Car Parts'), ('HG',
                                               'Home Goods'), ('FA', 'Fashion'), ('EL', 'Electronics')
    ]

    DURATION = timedelta(days=7)

    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='listing')
    time_left = models.DurationField(default=DURATION.days)
    created = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    category = models.CharField(
        choices=LISTING_CATEGORIES, max_length=40, default='Listing Category')
    title = models.CharField(max_length=64, default='')
    description = models.TextField(max_length=500, default='')
    slug = models.SlugField(max_length=250, unique_for_date='created')
    objects = models.Manager()

    def __str__(self):
        return self.title


class Bid(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bid')
    listing_id = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name='bid')
    posted = models.DateTimeField(default=timezone.now)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comment')
    content = models.TextField(max_length=500)
    posting = models.DateTimeField(default=timezone.now)


class Watchlist(models.Model):
    id = models.AutoField(primary_key=True)
    listing_id = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name='watchlist')
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='watchlist')
