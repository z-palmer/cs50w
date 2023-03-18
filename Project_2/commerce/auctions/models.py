from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    cash = models.DecimalField(max_digits=8, decimal_places=2)
    account_name = models.CharField(max_length=20, default='N/A')
    account_email = models.EmailField(max_length=64, default='N/A')


class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='listing')
    time_left = models.DurationField()
    created = models.DateTimeField(default=timezone.now)
    image = models.ImageField()


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
