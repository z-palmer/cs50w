from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone
from django.db import models
from datetime import timedelta


class Bid(models.Model):
    amount = models.CharField(max_length=64)
    id = models.AutoField(primary_key=True)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(max_length=500)


class Listing(models.Model):

    LISTING_CATEGORIES = [
        ('LC', 'Listing Category'), ('TY', 'Toys'), ('AN',
                                                     'Antiques'), ('ME', 'Memorabilia'),
        ('TO', 'Tools'), ('CA', 'Car Parts'), ('HG',
                                               'Home Goods'), ('FA', 'Fashion'), ('EL', 'Electronics')
    ]

    id = models.AutoField(primary_key=True)
    time_left = models.DurationField()
    posting = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    current_price = models.ForeignKey(
        Bid, on_delete=models.CASCADE, related_name='bid')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    objects = models.Manager()


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    cash = models.PositiveIntegerField(default=1000)
    listings = models.ForeignKey(Listing, on_delete=models.CASCADE, null=True)
    watchlist = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name='watchlist', null=True)
    bids = models.ForeignKey(Bid, on_delete=models.CASCADE, null=True)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
