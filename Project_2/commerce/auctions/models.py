from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.AutoField(primary_key=True)


class Listing(models.Model):

    class Category(models.TextChoices):
        LISTING_CATEGORY = 'Listing Category',
        TOYS = 'Toys',
        ANTIQUES = 'Antiques',
        MEMORABILIA = 'Memorabilia',
        TOOLS = 'Tools',
        CAR_PARTS = 'Car Parts',
        HOME_GOODS = 'Home Goods',
        FASHION = 'Fashion',
        ELECTRONICS = 'Electronics',

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    posting = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images')
    price = models.DecimalField(decimal_places=2, max_digits=7)
    description = models.TextField(max_length=300)
    category = models.CharField(max_length=100,
                                choices=Category.choices,
                                default=Category.LISTING_CATEGORY)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title


class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.DecimalField(decimal_places=2, max_digits=5)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, null=True, blank=True)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(max_length=500)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, null=True, blank=True)

    objects = models.Manager()


class WatchlistItem(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, null=True, blank=True)

    objects = models.Manager()
