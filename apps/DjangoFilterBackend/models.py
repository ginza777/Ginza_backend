from django.db import models
import random
# Create your models here.


class  Product(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    price = models.IntegerField(blank=True,null=True)
    price_max = models.IntegerField(blank=True,null=True)
    price_min = models.IntegerField(blank=True,null=True)
    code=models.IntegerField(blank=True,null=True)



    def save(self, *args, **kwargs):
        if not self.name:
            self.name = f"{self.pk} product"
        if not self.code:
            self.code=random.randint(100000,99999999)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name