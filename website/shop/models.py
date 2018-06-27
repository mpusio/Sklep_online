from django.db import models
from datetime import datetime
from django.conf import settings
# Create your models here.

class Categories(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class Products(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Orders(models.Model):
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Products, on_delete=models.CASCADE)
    text = models.TextField()