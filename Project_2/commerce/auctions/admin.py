from django.contrib import admin


from .models import User, Bid, Listing, Comment


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image',
                    'posting', 'initial_price')
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(User)
admin.site.register(Bid)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Comment)
