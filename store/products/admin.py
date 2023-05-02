from django.contrib import admin
from products.models import ProductCategory, Product, Basket

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('image', 'name', ('price', 'quantity'), 'category', 'description')
    # readonly_fields = ()
    search_fields = ('name',)
    ordering = ('name',)


