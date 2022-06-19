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

class Teacher(models.Model):
    surname = models.CharField("Фамилия", max_length=50)
    name = models.CharField("Имя", max_length=50)
    patr = models.CharField("Отчество", max_length=50)
    
    class Meta:
        db_table = "teachers"

class Subject(models.Model):
    level = models.CharField("Уровень", max_length=50)
    name = models.CharField("Название предмета", max_length=100)
    time = models.CharField("Время начала занятия", max_length=6)
    teacher = models.ForeignKey("Teacher", null=True, on_delete=models.SET_NULL)
    
    class Meta:
        db_table = "subjects"

class Lesson(models.Model):
    subjects = models.ForeignKey("Subject", null=True, on_delete=models.SET_NULL)
    topic = models.CharField("Тема", max_length=100)
    homework = models.CharField("Домашнее задание", max_length=500)
    date = models.CharField("Дата", max_length=10)
    
    class Meta:
        db_table = "lessons"

class Journal(models.Model):
    students = models.ForeignKey("Student", null=True, on_delete=models.SET_NULL)
    lessons = models.ForeignKey("Subject", null=True, on_delete=models.SET_NULL)
    mark = models.CharField("Оценка", max_length=1)
    
    class Meta:
        db_table = "journal"