from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.IntegerField(primary_key=True)
    cash = models.PositiveIntegerField(default=1000)


class Listing(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='listing')
    time_left = models.DurationField()
    posting = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()


class Bid(models.Model):
    amount = models.CharField(max_length=64)
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bid')
    listing_id = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name='bid')


class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comment')
    content = models.TextField(max_length=500)
