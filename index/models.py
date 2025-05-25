from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=32)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.category_name)

class Product(models.Model):
    product_name = models.CharField(max_length=128)
    product_des = models.TextField(blank=True)
    product_photo = models.ImageField(upload_to='media')
    create_date = models.DateTimeField(auto_now_add=True)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product_name)