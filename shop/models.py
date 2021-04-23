from django.db import models
from django_cryptography.fields import encrypt

# Create your models here.
class user(models.Model):
	name = models.CharField(max_length=256, null=False)
	email = models.EmailField(null=False)
	password = encrypt(models.CharField(max_length=256, null=False))
	street_address = models.CharField(max_length=500, null=True)
	city = models.CharField(max_length=20, null=True)
	state = models.CharField(max_length=2, null=True)
	zip = models.IntegerField(null=True)
	registration_date = models.DateTimeField(auto_now=True)

class item(models.Model):
	name = models.CharField(max_length=256, null=False)
	description = models.TextField(null=True)
	category = models.IntegerField(null=True)
	current_price = models.DecimalField(null=False, decimal_places=2, max_digits=8)
	rating = models.DecimalField(null=True, decimal_places=2, max_digits=2)

class ordered_item(models.Model):
	user_id = models.ForeignKey('user', on_delete=models.CASCADE)
	item_id = models.ForeignKey('item', on_delete=models.CASCADE)
	purchase_price = models.DecimalField(null=False, decimal_places=2, max_digits=8)
	purchase_date = models.DateTimeField(auto_now=True, null=False)