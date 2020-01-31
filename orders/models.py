from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Regular_pizza(models.Model):
    name=models.CharField(max_length=64)
    small=models.DecimalField(max_digits=4, decimal_places=2)
    large=models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.small} -{self.large}"

class Sicilian_pizza(models.Model):
    name=models.CharField(max_length=64)
    small=models.DecimalField(max_digits=4, decimal_places=2)
    large=models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.small} -{self.large}"

class Topping(models.Model):
    name=models.CharField(max_length=64)
    price =models.DecimalField(max_digits=4, decimal_places=2, default = 0.00)

    def __str__(self):
        return f"{self.name}"

class Sub(models.Model):
    name=models.CharField(max_length=64)
    small=models.DecimalField(max_digits=4, decimal_places=2)
    large=models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.small} -{self.large}"

class Salad(models.Model):
    name=models.CharField(max_length=64)
    price=models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}"

class Pasta(models.Model):
    name=models.CharField(max_length=64)
    price=models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}"

class Dinner_platter(models.Model):
    name=models.CharField(max_length=64)
    small=models.DecimalField(max_digits=4, decimal_places=2)
    large=models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.small} -{self.large}"

class my_order(models.Model):
    groupname = models.CharField(max_length=64 , default = "pizza")
    itemname = models.CharField(max_length=64)
    itemprice = models.DecimalField(max_digits=4, decimal_places=2)
    size = models.CharField(max_length=64 , default = "mediam")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.groupname} - {self.itemname} - {self.size} - {self.itemprice}"
    