from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.messages import get_messages, add_message

from .models import User, Listing


@login_required
def index(request):
    listings = Listing.objects.all()
    return render(request, "auctions/index.html", {
        'listings': listings
    })


@login_required
def listing(request, slug):
    pull = Listing.objects.get(slug=f'{slug}')
    return render(request, 'auctions/listing.html', {
        'title': pull.title, 'listing': pull
    })


@login_required
def add_to_watchlist(request, title):
    item = Listing.objects.get(title=title)
    json = User.objects.get(pk=id).watchlist
    json[title] = item.current_price
    return reverse(listing)


@login_required
def watchlist(request):
    pull = User.objects.get(pk=id).watchlist
    return render(request, 'auctions/watchlist.html', {
        'watchlist': pull
    })


@login_required
def categories(request):
    category_list = []
    for item in Listing.Category.choices:
        category_list.append(item[1])
    return render(request, 'auctions/categories.html', {'categories': category_list})


@login_required
def category_search(request, category):
    results = Listing.objects.filter(category=category)
    return render(request, 'auctions/category_search.html', {
        'results': results
    })


@login_required
def create_listing(request):
    return render(request, 'auctions/create_listing.html')


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
