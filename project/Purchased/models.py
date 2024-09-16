from django.db import models
from django.contrib.auth.models import User

class Purchased(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=33)
    description = models.CharField(max_length=250)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.author.username
