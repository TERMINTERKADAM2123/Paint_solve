from django.contrib import admin
from .models import Product ,Supplier
from django.contrib.auth.models import Group
# Register your models here.
admin.site.register(Product)
admin.site.register(Supplier)


