from django.db import models

# Create your models here.
class Electronics(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.IntegerField()
    available = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.name} {self.price}"