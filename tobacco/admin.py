from django.contrib import admin
from .models import Brands, TobaccoList, Inventory, Wishlist

admin.site.register(Brands)
admin.site.register(TobaccoList)
admin.site.register(Inventory)
admin.site.register(Wishlist)