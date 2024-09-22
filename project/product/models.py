from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
    title = models.CharField(max_length=33)
    description = models.CharField(max_length=250)
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/images/')
    def __str__(self):
        return self.title

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username






