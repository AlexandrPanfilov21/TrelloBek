from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length = 255)
    items = models.ForeignKey('Items', on_delete = models.PROTECT, null = True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Items(models.Model):
    item_name = models.CharField(max_length = 255)

    def __str__(self):
        return self.item_name