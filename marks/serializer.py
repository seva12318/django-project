from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from marks.models import School, Student, Teacher, Subject
  
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'surname', 'patr', 'school']  

class SchoolSerializer(serializers.ModelSerializer):
     class Meta:
        model = School
        fields = '__all__' 

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__' 

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__' 

class SchoolAddStudentsSerializer(serializers.Serializer):
    students = serializers.ListField(child=serializers.IntegerField()) 


