from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	birth_date = models.DateField(null=True, blank=True)
	age = models.PositiveIntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True)