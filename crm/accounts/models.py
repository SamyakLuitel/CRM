from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length =200, null = True)
    phone = models.IntegerField(max_length=20, null = True)
    email = models.EmailField(null=  True)
    date_created =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class Product(models.Model):
    CATEGORY =(
        ('Indoor','Indoor'),
        ('Out Door', 'Out  Door'),
        )
    name = models.CharField(max_length=50, null = True)
    price = models.FloatField(null = True)
    category = models.CharField(max_length =200, null =True , choices = CATEGORY)
    description = models.CharField(max_length = 200, null = True)
    data_created = models.DateTimeField(auto_now_add=True, null=  True)


class Order(models.Model):
    #customer = 
    #product =
    STATUS =(
        ('Pending','Pending'),
        ('Out of delivery', 'Out of delivery'),
        ('Delivered', 'Delivered'),
        )
    date_created = models.DateTimeField(auto_now_add=True, null =True)
    status  = models.CharField(max_length= 200, null = True, choices = STATUS)

