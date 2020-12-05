from django.db import models

# Create your models here.
class employee(models.Model):
    idno = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    salary = models.FloatField()
