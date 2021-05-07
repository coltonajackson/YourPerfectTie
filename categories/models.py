from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

class Category(models.Model):
    GENDER_BOOL_CHOICES = ((True, 'Male'), (False, 'Female'))
    AGE_BOOL_CHOICES = ((True, 'Adult'), (False, 'Youth'))
    name = models.CharField(max_length=256, null=False)
    gender = models.BooleanField(null=True, choices=GENDER_BOOL_CHOICES)
    age_group = models.BooleanField(null=True, choices=AGE_BOOL_CHOICES)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'pk': str(self.pk)})