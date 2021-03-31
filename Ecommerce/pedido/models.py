from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()