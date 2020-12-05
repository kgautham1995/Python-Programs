from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)
    salary=models.FloatField()
