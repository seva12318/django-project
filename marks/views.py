from django.shortcuts import render
from django.views import View
from django.http import JsonResponse 
from marks.models import Choice, Lesson, School, Student, Subject, Teacher
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
# Создаем здесь представления. 
def home(request):
    return render(request,"marks/home.html")

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
# Create your views here.
class StudentView(View):
    def get(request, *args):
        students = list(Student.objects.all().values())

        return JsonResponse({
            "students": list(students)
        })

class OneStudentView(View):
    def get(request, *args, **kwargs):
        id = kwargs['id']
        student: Student = Student.objects.select_related("school").get(id=id)
        #school: School = student.school
        return JsonResponse({
            "name": student.name,
            "surname": student.surname,
            "patronimic": student.patr,
            "school": student.school.title,
        })

class SchoolView(View):
    def get(request, *args):
        schools = list(School.objects.all().values())

        return JsonResponse({
            "schools": list(schools)
        })

class OneSchoolView(View):
    def get(request, *args, **kwargs):
        id = kwargs['id']
        school: School = School.objects.get(id=id)
        #school: School = student.school
        return JsonResponse({
            "title": school.title,
        })

class TeacherView(View):
    def get(request, *args):
        teachers = list(Teacher.objects.all().values())

        return JsonResponse({
            "teachers": list(teachers)
        })

class OneTeacherView(View):
    def get(request, *args, **kwargs):
        id = kwargs['id']
        teacher: Teacher = Teacher.objects.get(id=id)
        #school: School = student.school
        return JsonResponse({
            "name": teacher.name,
            "surname": teacher.surname,
            "patronimic": teacher.patr,
        })

class SubjectView(View):
    def get(request, *args):
        subjects = list(Subject.objects.all().values())

        return JsonResponse({
            "subjects": list(subjects)
        })

class OneSubjectView(View):
    def get(request, *args, **kwargs):
        id = kwargs['id']
        subject: Subject = Subject.objects.select_related("teacher").get(id=id) 
        return JsonResponse({
            "name": subject.name,
            "level": subject.level,
            "time": subject.time,
            "teacher": subject.teacher.surname + ' ' + subject.teacher.name + ' ' + subject.teacher.patr
        })

class LessonView(View):
    def get(request, *args):
        lessons = list(Lesson.objects.all().values())

        return JsonResponse({
            "lessons": list(lessons)
        })

class OneLessonView(View):
    def get(request, *args, **kwargs):
        id = kwargs['id']
        lesson: Lesson = Lesson.objects.select_related("subjects").get(id=id)
        #school: School = student.school
        return JsonResponse({
            "subject": lesson.subjects.name,
            "topic": lesson.topic,
            "homework": lesson.homework,
            "date": lesson.date,
        })

class ChoicesView(View):
    def get(request, *args):
        choices = list(Choice.objects.all().values())

        return JsonResponse({
            "choices": list(choices)
        })


        



