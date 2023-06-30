from django.db import models

# Create your models here.
class Coffee(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='photoes/', null=True)

    def __str__(self):
        return self.name

