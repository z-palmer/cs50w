from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone
from django.db import models
from datetime import timedelta, datetime


class Bid(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=5)


class Comment(models.Model):
    content = models.TextField(max_length=500)


class Listing(models.Model):

    LISTING_CATEGORIES = [

        ('LC', 'Listing Category'),
        ('TY', 'Toys'),
        ('AN', 'Antiques'),
        ('ME', 'Memorabilia'),
        ('TO', 'Tools'),
        ('CA', 'Car Parts'),
        ('HG', 'Home Goods'),
        ('FA', 'Fashion'),
        ('EL', 'Electronics')

    ]

    title = models.CharField(max_length=100)
    time_left = models.DurationField()
    posting = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images')
    initial_price = models.DecimalField(decimal_places=2, max_digits=5)
    current_price = models.ForeignKey(
        Bid, on_delete=models.CASCADE, related_name='bid', blank=True, null=True)
    comments = models.ForeignKey(
        Comment, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(max_length=300)
    slug = models.SlugField(max_length=250, unique_for_date='posting')

    objects = models.Manager()

    def __str__(self):
        return self.title


class User(AbstractUser):
    cash = models.PositiveIntegerField(default=1000)
    listings = models.ForeignKey(
        Listing, on_delete=models.CASCADE, null=True, blank=True)
    watchlist = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name='watchlist', null=True, blank=True)
    bids = models.ForeignKey(
        Bid, on_delete=models.CASCADE, null=True, blank=True)
    comments = models.ForeignKey(
        Comment, on_delete=models.CASCADE, null=True, blank=True)
