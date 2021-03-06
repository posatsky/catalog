from django.db import models
from django.shortcuts import reverse

# Create your models here.
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    price = models.CharField(max_length=150, db_index=True)
    date_add = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('product_datail_url', kwargs={'slug': self.slug}) # revers for py file link for post detail 

    def __str__(self):
        return '{}'.format(self.title)
