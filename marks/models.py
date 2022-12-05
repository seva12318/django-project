from statistics import mode
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField("Имя", max_length=50)
    surname = models.CharField("Фамилия", max_length=50)
    patr = models.CharField("Отчество", max_length=50)
    school = models.ForeignKey("School", null=True, on_delete=models.CASCADE,  verbose_name = 'Школа')
    num_class = models.CharField("Класс", max_length=3, null=True)

    def __str__(self):
        return f'{self.surname} {self.name} {self.patr}'
    
    class Meta:
        db_table = "students"

class School(models.Model):
    title = models.CharField("Наименование школы", max_length=100)
    
    class Meta:
        db_table = "school"

    def __str__(self):
        return f'{self.title}'

class Teacher(models.Model):
    surname = models.CharField("Фамилия", max_length=50)
    name = models.CharField("Имя", max_length=50)
    patr = models.CharField("Отчество", max_length=50)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.surname} {self.name} {self.patr}'

    class Meta:
        db_table = "teachers"

class Subject(models.Model):
    level = models.CharField("Уровень", max_length=50)
    name = models.CharField("Название предмета", max_length=100)
    time = models.CharField("Время начала занятия", max_length=6)
    teacher = models.ForeignKey("Teacher", null=True, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "subjects"
    
    def __str__(self):
        return f'{self.name} ({self.level})'

class Lesson(models.Model):
    subjects = models.ForeignKey("Subject", null=True, on_delete=models.CASCADE, verbose_name = 'Название предмета')
    topic = models.CharField("Тема", max_length=100)
    homework = models.CharField("Домашнее задание", max_length=500, blank=True)
    date = models.CharField("Дата", max_length=10)
    
    class Meta:
        db_table = "lessons"
    
    def __str__(self):
        return f'{self.topic}'

class Journal(models.Model):
    students = models.ForeignKey("Student", null=True, on_delete=models.CASCADE,  verbose_name = 'ФИО студента')
    lessons = models.ForeignKey("Lesson", null=True, on_delete=models.CASCADE, verbose_name = 'Тема урока')
    mark = models.CharField("Оценка", max_length=1)
    
    class Meta:
        db_table = "journal"


class Choice(models.Model):
    students = models.ForeignKey("Student", null=True, on_delete=models.CASCADE, verbose_name = 'ФИО студента')
    year = models.CharField("Год", max_length=4)
    semester = models.CharField("Семестр", max_length=1)
    sub_first = models.ForeignKey("Subject", null=True, on_delete=models.CASCADE, related_name="sub_first", verbose_name = 'Предмет № 1')
    sub_second = models.ForeignKey("Subject", null=True, on_delete=models.CASCADE, related_name="sub_second", verbose_name = 'Предмет № 2') 

    class Meta:
        db_table = "choices"
