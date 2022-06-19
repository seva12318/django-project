from django.shortcuts import render
from django.views import View
from django.http import JsonResponse 

from marks.models import School, Student

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