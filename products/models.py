from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from categories.models import Category

class Product(models.Model):
	name = models.CharField(max_length=256, null=False)
	description = models.TextField(null=True)
	main_image = models.ImageField(upload_to='images/', blank=True)
	current_price = models.DecimalField(null=False, decimal_places=2, max_digits=8)
	rating = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=2)
	created_at = models.DateTimeField(auto_now_add=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	publisher = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	def get_display_price(self):
		return "{0:2f}".format(self.current_price)

	def get_absolute_url(self):
		return reverse('product_detail', kwargs={'pk': str(self.pk)})

class Comment(models.Model):
	product = models.ForeignKey(
		Product, 
		on_delete=models.CASCADE,
		related_name='comments',
	)
	comment = models.TextField(null=True)
	publisher = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.comment

	def get_absolute_url(self):
		return reverse('product_list')