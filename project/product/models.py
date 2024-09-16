from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=33)
    description = models.CharField(max_length=250)
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/images/')


    def __str__(self):
        return self.title





