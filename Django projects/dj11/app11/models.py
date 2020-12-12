from django.db import models

# Create your models here.
class studentmodel(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
    ContactNo = models.IntegerField()
    Registered_Course= models.CharField(max_length=50)
    Validity=models.IntegerField()
