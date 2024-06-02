from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField()