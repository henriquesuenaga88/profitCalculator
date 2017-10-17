from django.db import models
from product.models import Product, Unity

class Portion(models.Model):
    ingredient = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unity = models.ForeignKey(Unity, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {} {}'.format(self.ingredient.name, self.quantity, self.unity.initials)

class Recipe(models.Model):
    name = models.CharField(max_length=50, unique=True)
    portion = models.ManyToManyField(Portion)
    unity_yield = models.IntegerField()

    def __str__(self):
        return self.name
