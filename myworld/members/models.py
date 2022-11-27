from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mail = models.EmailField()
    phone = models.CharField(max_length=30)
    id = models.CharField(max_length=30, primary_key=True)
    gender = models.CharField(max_length=10, default="")
    date_of_birth = models.DateField()
    level = models.IntegerField()
    gpa = models.FloatField()
    status = models.CharField(max_length=20,  default="")
    department = models.CharField(max_length=30, default="General")
