from dataclasses import fields
from imp import source_from_cache
from rest_framework import serializers
import lessons
from marks.models import Journal, Lesson, School, Student, Teacher, Subject, Choice
  
class StudentSerializer(serializers.ModelSerializer):
    school_title = serializers.CharField(source="school.title", read_only=True)
    class Meta:
        model  =Student
        fields = ['id', 'name', 'surname', 'patr', 'school', 'school_title', 'num_class']  

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
    subjects_name = serializers.CharField(source="subjects.__str__", read_only=True) 
    class Meta:
        model = Lesson
        fields = ['id', 'subjects', 'subjects_name', 'topic', 'homework', 'date']

class JournalSerializer(serializers.ModelSerializer):
    students_name = serializers.CharField(source="students.__str__", read_only=True)
    #lessons = serializers.CharField(source="lessons.subjects.name", read_only=True)

    class Meta:
        model = Journal
        fields = ['id', 'students', 'students_name', 'lessons', 'mark'] 

class ChoiceSerializer(serializers.ModelSerializer):
    sub_first_name = serializers.CharField(source="sub_first.__str__", read_only=True)
    sub_second_name = serializers.CharField(source="sub_second.__str__", read_only=True) 
    students_name = serializers.CharField(source="students.__str__", read_only=True)
    #sub_first_level = serializers.CharField(source="sub_first.level", read_only=True) на случай если уровень понадобится отправлять отдельно
    #sub_second_level = serializers.CharField(source="sub_second.level", read_only=True) на случай если уровень понадобится отправлять отдельно
    class Meta:
        model = Choice
        fields = ['id', 'students', 'students_name', 'year', 'semester', 'sub_first', 'sub_first_name', 'sub_second', 'sub_second_name']

class SchoolAddStudentsSerializer(serializers.Serializer):
    students = serializers.ListField(child=serializers.IntegerField()) 

class LessonAddMarkSerializer(serializers.Serializer):
    #jouurnal = serializers.ListField(child=serializers.IntegerField())  
    class Meta:
        model = Journal
        fields = ['students', 'lessons', 'mark']

class JournalReportSerializer(serializers.ModelSerializer):
    students_name = serializers.CharField(source="students.__str__", read_only=True)
    lessons_name = serializers.CharField(source="lessons.subjects.__str__", read_only=True)
    date = serializers.CharField(source="lessons.date", read_only=True)
    num_class = serializers.CharField(source="students.num_class", read_only=True)
    class Meta:
        model = Journal
        fields = ['students', 'students_name', 'num_class', 'lessons', 'date', 'lessons_name', 'mark'] 

class IdUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id']