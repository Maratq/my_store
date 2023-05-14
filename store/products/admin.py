from django.contrib import admin

from products.models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('image', 'name', ('price', 'quantity'),'stripe_product_price_id', 'category', 'description')
    # readonly_fields = ()
    search_fields = ('name',)
    ordering = ('name',)


