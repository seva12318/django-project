from turtle import title
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField("Имя", max_length=50)
    surname = models.CharField("Фамилия", max_length=50)
    patr = models.CharField("Отчество", max_length=50)
    school = models.ForeignKey("School", null=True, on_delete=models.SET_NULL)
    
    class Meta:
        db_table = "students"

class School(models.Model):
    title = models.CharField("Наименование школы", max_length=100)
    
    class Meta:
        db_table = "school"