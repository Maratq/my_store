from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return f'{self.name} {self.description}'

class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images',null=True,blank=True)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)


    def __str__(self):
        return f'Продукт - {self.name} | Категория - {self.category}'