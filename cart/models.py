from django.db import models
from django.db import models

class CartItem(models.Model):
    product = models.ForeignKey('app.Tovar', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
# Create your models here.
