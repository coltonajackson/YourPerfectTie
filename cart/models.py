from django.db import models

# Create your models here.
from django.db import models
from users.models import CustomUser
from products.models import Product

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(blank=True)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)

    def __str__(self):
        return self.product