from django.db import models
from datetime import datetime
from users.models import CustomUser
from items.models import Item

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)

class CartItem(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price_ht = models.FloatField(blank=True)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)