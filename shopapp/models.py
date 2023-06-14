from django.db import models


# Create your models here.
class firstdb(models.Model):
    Name=models.CharField(max_length=20, null=True,blank=True)
    Types=models.CharField(max_length=50, null=True,blank=True)
    Description=models.CharField( max_length=100,null=True,blank=True)
    Image=models.ImageField(upload_to="profile",null=True,blank=True)

class seconddb(models.Model):
    Name=models.CharField(max_length=20, null=True,blank=True)
    Category=models.CharField(max_length=50, null=True,blank=True)
    Colour=models.CharField(max_length=100,null=True,blank=True)
    Price=models.IntegerField( null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Description=models.CharField( max_length=100,null=True,blank=True)
    Image=models.ImageField(upload_to="profile",null=True,blank=True)

