from django.db import models
from django.urls import reverse

from commerce.settings import AUTH_USER_MODEL

# Create your models here.

# model Product

class Product(models.Model):
    name=models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    price=models.FloatField(default=0.0)
    stock=models.PositiveIntegerField(default=0)
    description=models.TextField(blank=True)
    image=models.ImageField(blank=True,null=True,upload_to="products")

    def __str__(self):
        return f"{self.name} ({self.stock})"
    
    def get_absolute_url(self):
        return reverse("product", kwargs={"slug":self.slug})
    
class Order(models.Model):
    user= models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.IntegerField(default=1)
    ordered= models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

class Cart(models.Model):
    user=  models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders= models.ManyToManyField(Order)
    ordered= models.BooleanField(default=False)
    ordered_date= models.TimeField(blank=True, null=True)
    def __str__(self):
        return self.user.username
