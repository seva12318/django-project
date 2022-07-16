from dataclasses import fields
from rest_framework import serializers
import lessons
from marks.models import Journal, Lesson, School, Student, Teacher, Subject, Choice
  
class StudentSerializer(serializers.ModelSerializer):
    school = serializers.CharField(source="school.title", read_only=True)
    class Meta:
        model  =Student
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
    teacher = serializers.CharField(source="teacher.__str__" , read_only=True)
    class Meta:
        model = Subject
        fields = ['level', 'name', 'time', 'teacher'] 

class LessonSerializer(serializers.ModelSerializer):
    subjects = serializers.CharField(source="subjects.name", read_only=True) 
    class Meta:
        model = Lesson
        fields = ['subjects', 'topic', 'homework', 'date']

class JournalSerializer(serializers.ModelSerializer):
    students = serializers.CharField(source="students.__str__", read_only=True)
    #lessons = serializers.CharField(source="lessons.subjects.name", read_only=True)

    class Meta:
        model = Journal
        fields = ['students', 'lessons', 'mark'] 

class ChoiceSerializer(serializers.ModelSerializer):
    sub_first = serializers.CharField(source="sub_first.name", read_only=True)
    sub_second = serializers.CharField(source="sub_second.name", read_only=True) 
    students = serializers.CharField(source="students.__str__", read_only=True)
    class Meta:
        model = Choice
        fields = ['students', 'year', 'semester', 'sub_first', 'sub_second', 'num_class']

class SchoolAddStudentsSerializer(serializers.Serializer):
    students = serializers.ListField(child=serializers.IntegerField()) 

class LessonAddMarkSerializer(serializers.Serializer):
    #jouurnal = serializers.ListField(child=serializers.IntegerField())  
    class Meta:
        model = Journal
        fields = ['students', 'lessons', 'mark']



