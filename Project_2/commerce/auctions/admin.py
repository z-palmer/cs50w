from django.contrib import admin


from .models import User, Bid, Listing, Comment, WatchlistItem


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image',
                    'posting', 'price')


class BidAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'listing')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'listing')


class WatchlistItemAdmin(admin.ModelAdmin):
    list_dsplay = ('user', 'listing')


# Register your models here.
admin.site.register(User)
admin.site.register(Bid, BidAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(WatchlistItem, WatchlistItemAdmin)
