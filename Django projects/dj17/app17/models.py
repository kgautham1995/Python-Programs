from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    salary = models.FloatField()
    designation = models.CharField(max_length=50,unique=True)
    photo = models.ImageField(upload_to="employee_images/")
    file=models.FileField(upload_to="employee_docs/")