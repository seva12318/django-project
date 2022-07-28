from dataclasses import fields
from rest_framework import serializers
import lessons
from marks.models import Journal, Lesson, School, Student, Teacher, Subject, Choice
  
class StudentSerializer(serializers.ModelSerializer):
    school_title = serializers.CharField(source="school.title", read_only=True)
    class Meta:
        model  =Student
        fields = ['id', 'name', 'surname', 'patr', 'school', 'school_title']  

class SchoolSerializer(serializers.ModelSerializer):
     class Meta:
        model = School
        fields = '__all__' 

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__' 

class SubjectSerializer(serializers.ModelSerializer):
    teacher_fio = serializers.CharField(source="teacher.__str__" , read_only=True)
    class Meta:
        model = Subject
        fields = ['id', 'level', 'name', 'time', 'teacher', 'teacher_fio'] 

class LessonSerializer(serializers.ModelSerializer):
    subjects_name = serializers.CharField(source="subjects.name", read_only=True) 
    class Meta:
        model = Lesson
        fields = ['id', 'subjects', 'subjects_name', 'topic', 'homework', 'date']

class JournalSerializer(serializers.ModelSerializer):
    students_name = serializers.CharField(source="students.__str__", read_only=True)
    #lessons = serializers.CharField(source="lessons.subjects.name", read_only=True)

    class Meta:
        model = Journal
        fields = ['students', 'students_name', 'lessons', 'mark'] 

class ChoiceSerializer(serializers.ModelSerializer):
    sub_first_name = serializers.CharField(source="sub_first.name", read_only=True)
    sub_second_name = serializers.CharField(source="sub_second.name", read_only=True) 
    students_name = serializers.CharField(source="students.__str__", read_only=True)
    class Meta:
        model = Choice
        fields = ['students', 'students_name', 'year', 'semester', 'sub_first', 'sub_first_name', 'sub_second', 'sub_second_name', 'num_class']

class SchoolAddStudentsSerializer(serializers.Serializer):
    students = serializers.ListField(child=serializers.IntegerField()) 

class LessonAddMarkSerializer(serializers.Serializer):
    #jouurnal = serializers.ListField(child=serializers.IntegerField())  
    class Meta:
        model = Journal
        fields = ['students', 'lessons', 'mark']


