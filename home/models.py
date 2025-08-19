from django.db import models

# Create your models here.

class Student(models.Model):
    
    # id = models.AutoField()
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    image = models.ImageField(upload_to='media')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    
    
class Product(models.Model):
    pass