from django.db import models

class Unity(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    initials = models.CharField(max_length=2, default="XX")

    def __str__(self):
        return '{} - {}'.format(self.name, self.initials)

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    amount = models.IntegerField()
    unity = models.ForeignKey(Unity, on_delete=models.CASCADE)

    def __str__(self):
        return '{},  {} {}  -  R${}'.format(self.name, self.amount, self.unity.initials, self.price)
