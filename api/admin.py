from django.contrib import admin
from .models import Order, Product, OrderItem

# Register your models here.
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(OrderItem)