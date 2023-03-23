from django.contrib import admin


from .models import User, Bid, Listing, Comment


class ListingAdmin(admin.ModelAdmin):
    list_filter = ('title', 'price', 'category', 'created', 'time_left')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created'


# Register your models here.
admin.site.register(User)
admin.site.register(Bid)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Comment)
