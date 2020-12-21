from django.db import models

class EmployeeModel(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    salary = models.FloatField()
    designation = models.CharField(max_length=50)
    contactno = models.IntegerField(unique=True)
    password = models.CharField(max_length=50)