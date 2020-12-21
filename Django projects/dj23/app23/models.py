from django.db import models

class Common(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    contactno = models.IntegerField(unique=True)
    email = models.EmailField(unique=True, max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        abstract = True


class HODModel(Common):
    salary = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "HOD"

class FacultyModel(Common):
    salary = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Faculty"

class StudentModel(Common):
    marks = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Student"


class ParentModel(models.Model):

    gen = (('Male','Male'),('Female','Female'))

    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contactno = models.IntegerField(unique=True)
    gender = models.CharField(choices=gen,max_length=30)