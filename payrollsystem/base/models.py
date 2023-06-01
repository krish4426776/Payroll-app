from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    USER_TYPES = (
        
        ('seller', 'Seller'),
        ('buyer', 'Buyer'),
    )
    user_type= models.CharField(max_length=10, choices=USER_TYPES)

class Seller(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True) # for every seller, there is exactly one user associated with them, and for every user, there is exactly one seller associated with them.
    def __str__(self):
        return self.user.username 
class Buyer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return self.user.username 

class Bill(models.Model):
    STATUS =(
        ('fulfilled' , 'FULFILLED'),
        ('unfulfilled' , 'UNFULFILLED'),
    )
    seller = models.ForeignKey(Seller , on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer , on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20 , choices=STATUS , default='unfulfilled')

    def __str__ (self):
        return f"{self.seller} - {self.buyer}"