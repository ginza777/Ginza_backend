from django.contrib import admin

from apps.DjangoFilterBackend.models import Product


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'price_min', 'price', 'price_max']
    list_editable = ['price','price_max', 'price_min']