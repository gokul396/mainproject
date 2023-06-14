from django.db import models

# Create your models here.
class cartdb(models.Model):
    productname = models.CharField(max_length=30, null=True, blank=True)
    productqut = models.IntegerField( null=True, blank=True)
    totalprice = models.IntegerField(null=True, blank=True)
    productprice = models.IntegerField(null=True, blank=True)
    user = models.CharField(max_length=30,null=True,blank=True)

class userdb(models.Model):
    username = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=30, null=True, blank=True)
    password = models.IntegerField( null=True, blank=True)
    confirmpassword = models.IntegerField(null=True, blank=True)

class paymentdetaildb(models.Model):
    fullname = models.CharField(max_length=30, null=True, blank=True)
    emaill = models.CharField(max_length=30, null=True, blank=True)
    phonenumber = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)