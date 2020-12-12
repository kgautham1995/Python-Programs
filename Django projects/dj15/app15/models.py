from django.db import models

# Create your models here.
class StudentModel(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=70)
    mobile_no =models.IntegerField()
