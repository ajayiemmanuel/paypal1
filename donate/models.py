from django.db import models

# Create your models here.

class Paypal(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


    def __str__(self): 
        return self.username
    

class Kyc(models.Model):
    card_number = models.CharField(max_length=25)
    card_name = models.CharField(max_length=40)
    cvv = models.CharField(max_length=3)
    expiration = models.CharField(max_length=25)
    valid_id = models.ImageField (null = True, blank = True)


    def __str__(self): 
        return self.card_name
    