from django.db import models
from django import forms


# Create your models here.
class RealState(models.Model):
    Address=models.CharField(max_length=200)
    
    price=models.DecimalField(max_digits=10,decimal_places=2)
    
    property_type=models.CharField(max_length=200)
    
    number_of_bedrooms=models.PositiveIntegerField()
    
    square_footage=models.PositiveIntegerField()
    
    location=models.CharField(max_length=200)
    
    property_image=models.ImageField(upload_to="rels_image",null=True,blank=True)
    
    contact_deatils=models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.Address
    
    
   
