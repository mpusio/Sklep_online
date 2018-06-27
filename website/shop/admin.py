from django.contrib import admin

# Register your models here.
from .models import Categories
from .models import Products
from .models import Orders

admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Orders)
