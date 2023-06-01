from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .models import CustomUser, Seller, Buyer ,Bill

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(Bill)