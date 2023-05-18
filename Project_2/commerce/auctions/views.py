from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import User, Listing, WatchlistItem, Comment
from .forms import ListingForm, CommentForm, BidForm


def index(request):
    listings = Listing.objects.all()
    return render(request, "auctions/index.html", {
        'listings': listings
    })


@login_required
def listing(request, title):
    added = False
    pull = Listing.objects.get(title=f'{title}')
    if WatchlistItem.objects.filter(user=request.user, listing=pull):
        added = True
    else:
        added = False
    comments = Comment.objects.filter(listing=pull)
    return render(request, 'auctions/listing.html', {
        'title': pull.title, 'listing': pull, 'added': added, 'comments': comments
    })


@login_required
def add_comment(request, title):
    pull = Listing.objects.get(title=title)
    if request.method == 'POST':
        new_comment_form = CommentForm(request.POST)
        if new_comment_form.is_valid():
            new_comment = new_comment_form.save()
            new_comment.listing = pull
            new_comment.user = request.user
            new_comment.save()
            return HttpResponseRedirect(reverse('listing', args=[title]))
    else:
        new_comment_form = CommentForm()
        return render(request, 'auctions/add_comment.html', {
            'form': new_comment_form
        })


@login_required
def add_bid(request, title):
    pull = Listing.objects.get(title=title)
    if request.method == 'POST':
        new_bid_form = BidForm(request.POST)
        if float(request.POST['amount']) > float(pull.price):
            if new_bid_form.is_valid():
                new_bid = new_bid_form.save()
                pull.price = new_bid.amount
                pull.highest_bidder = request.user
                pull.save()
                new_bid.listing = pull
                new_bid.user = request.user
                new_bid.save()
                return HttpResponseRedirect(reverse('listing', args=[title]))
        else:
            messages.error(
                request, 'Bid must be higher than the original amount of the listing.')
            return HttpResponseRedirect(reverse('listing', args=[title]))
    else:
        new_bid_form = BidForm()
        return render(request, 'auctions/add_bid.html', {
            'form': new_bid_form
        })


@login_required
def close_listing(request, title):
    pull = Listing.objects.get(title=title)
    pull.closed = True
    pull.save()
    return HttpResponseRedirect(reverse('listing', args=[title]))


@login_required
def add_to_watchlist(request, listing_id):
    user = request.user
    pull = Listing.objects.get(id=listing_id)
    item = WatchlistItem(user=user, listing=pull)
    item.save()
    return HttpResponseRedirect(reverse('listing', args=[pull.title]))


@login_required
def remove_from_watchlist(request, listing_id):
    user = request.user
    pull = Listing.objects.get(id=listing_id)
    item = WatchlistItem.objects.filter(user=user, listing=pull)
    item.delete()
    return HttpResponseRedirect(reverse('listing', args=[pull.title]))


@login_required
def watchlist(request):
    items = WatchlistItem.objects.filter(user=request.user)
    return render(request, 'auctions/watchlist.html', {
        'watchlist': items
    })


@login_required
def categories(request):
    category_list = []
    for item in Listing.Category.choices:
        category_list.append(item[1])
    return render(request, 'auctions/categories.html', {
        'categories': category_list
    })


@login_required
def category_search(request, category):
    results = Listing.objects.filter(category=category)
    return render(request, 'auctions/category_search.html', {
        'results': results
    })


@login_required
def create_listing(request):
    if request.method == 'POST':
        new_listing_form = ListingForm(request.POST, request.FILES)
        if new_listing_form.is_valid:
            new_listing = new_listing_form.save()
            new_listing.user = request.user
            new_listing.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            print(new_listing_form.errors)
    else:
        new_listing_form = ListingForm()
        return render(request, 'auctions/create_listing.html', {
            'new_listing': new_listing_form
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
