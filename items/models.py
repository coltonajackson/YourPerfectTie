from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

class Item(models.Model):
	name = models.CharField(max_length=256, null=False)
	description = models.TextField(null=True)
	category = models.IntegerField(null=True)
	current_price = models.DecimalField(null=False, decimal_places=2, max_digits=8)
	rating = models.DecimalField(null=True, decimal_places=2, max_digits=2)
	created_at = models.DateTimeField(auto_now_add=True)
	publisher = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('item_detail', args=[str(self.id)])

class Comment(models.Model):
	item = models.ForeignKey(
		Item, 
		on_delete=models.CASCADE,
		related_name='comments',
	)
	comment = models.TextField(null=True)
	publisher = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

	def __str__(self):
		return self.comment

	def get_absolute_url(self):
		return reverse('item_list')