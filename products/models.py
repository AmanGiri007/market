from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.


class Product(models.Model):
    stock_available = models.IntegerField(
        default=0, validators=[MinValueValidator(0)])
    product_name = models.CharField(max_length=35)
    product_rate = models.IntegerField()
    product_image = models.ImageField(upload_to="product-images")
    product_description = models.TextField()

    def __str__(self):
        return f" {self.id} {self.product_name}"
