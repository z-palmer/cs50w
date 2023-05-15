from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('listing/<str:title>', views.listing, name='listing'),
    path('categories', views.categories, name='categories'),
    path('category_search/<str:category>',
         views.category_search, name='category_search'),
    path('create-listing', views.create_listing, name='create_listing'),
    path('watchlist', views.watchlist, name='watchlist'),
    path('add_to_watchlist/<str:listing_id>',
         views.add_to_watchlist, name='add_to_watchlist'),
    path('remove_from_watchlist/<str:listing_id>',
         views.remove_from_watchlist, name='remove_from_watchlist'),
    path('add_comment/<str:title>', views.add_comment, name='add_comment'),
    path('add_bid/<str:title>', views.add_bid, name='add_bid'),
    path('close_listing/<str:title>', views.close_listing, name='close_listing'),

]
