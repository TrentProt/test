from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

class Basket(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.item

class PDF(models.Model):
    number = models.CharField(max_length=10)
    img = models.ImageField(upload_to='media/qrcodes', null=True, blank=True)
    file = models.FileField(upload_to='media', null=True, blank=True)
