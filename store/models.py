from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey

# Create your models here.


class customer(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.id

# category model

class category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


# product model

class product(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    category_id = models.ForeignKey(category, default='doors', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    info = models.TextField(max_length=400)
    price = models.IntegerField(default=199)
    quantity = models.IntegerField(default=1)
    image = models.ImageField(upload_to='pics', height_field=None, width_field=None,)


    def __str__(self):
        return self.id
        


class orders(models.Model):
    order_id = models.CharField(primary_key=True, max_length=10)
    customer_id = models.ForeignKey(customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_id