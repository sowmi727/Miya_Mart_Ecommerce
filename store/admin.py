from django.contrib import admin
from .models import Product, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'subcategory', 'price')
    list_filter = ('category', 'subcategory')
    search_fields = ('name', 'category', 'subcategory')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'customer_name',
        'phone',
        'total_amount',
        'payment_method',
        'payment_status',
        'order_date'
    )
    list_editable = ('payment_status',)
  