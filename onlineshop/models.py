from django.db import models

# Create your models here.

# The `timestampModel` class is an abstract model in Python with `created_at` and `updated_at` fields
# that automatically track creation and update timestamps.
class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True

# This Python class defines a model for a category with attributes for category name and description.
class Category(TimestampModel):
    category_name = models.CharField(max_length= 185)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.category_name
    

# The `Product` class defines a model with fields for product name, description, price, image, and
# category in a Django application.
class Product(TimestampModel):
    product_name = models.CharField(max_length=170)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
    

class Order(TimestampModel):
    customer_name = models.CharField(max_length=180)
    customer_email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Order #{self.id}"
    
