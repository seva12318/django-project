from gc import get_objects
from msilib.schema import Class
from rest_framework import viewsets, renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from marks.models import Choice, Journal, Lesson, School, Student, Subject, Teacher
from marks.serializer import ChoiceSerializer, JournalSerializer, LessonSerializer, SchoolAddStudentsSerializer, SchoolSerializer, StudentSerializer, SubjectSerializer, TeacherSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset =  Student.objects.all()
    serializer_class = StudentSerializer
    renderer_classes = [renderers.JSONRenderer]

    def get_queryset(self):
        return Student.objects.all()
    
    @action(detail=True, url_path="choice", methods=['GET'])
    def students(self, *args, **kwargs):
        current_student= self.get_object()
        choice = Choice.objects.filter(students=current_student)
        serializer = ChoiceSerializer(choice, many=True)
        data = serializer.data

        return Response({
            "students-choices": data,
        })

class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    renderer_classes = [renderers.JSONRenderer]

    def get_queryset(self):
        return Journal.objects.all()  

    @action(detail=True, url_path="lesson", methods=['GET'])
    def students(self, *args, **kwargs):
        journal = Journal.objects.filter(lessons=self.kwargs['pk'])
        serializer = JournalSerializer(journal, many=True)
        data = serializer.data
        return Response({
           "journal": data, 
        })

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    renderer_classes = [renderers.JSONRenderer]

    def get_queryset(self):
        return Lesson.objects.all()    

class SchoolViewSet(viewsets.ModelViewSet):
    queryset =  School.objects.all()
    serializer_class = SchoolSerializer
    renderer_classes = [renderers.JSONRenderer]

    @action(detail=True, url_path="students", methods=['GET'])
    def students(self, *args, **kwargs):
        current_school = self.get_object()
        students = Student.objects.filter(school=current_school)
        
        serializer = StudentSerializer(students, many=True)
        data = serializer.data

        return Response({
           "students": data, 
        })

    @action(detail=True, url_path="add-students", methods=['POST'])
    def add_students(self,request, *args, **kwargs):
 
        current_school = self.get_object()

        serializer = SchoolAddStudentsSerializer(data=self.request.data)
        serializer.is_valid(True)
        data = serializer.validated_data

        Student.objects.filter(id__in=data['students']).update(school=current_school)

        return Response(status=200)
    
    @action(detail=False, url_path="odd", methods=['GET'])
    def odd_schools(self,*args, **kwargs):
        schools = School.objects.filter(id__in = (1,3))
        return Response(SchoolSerializer(schools, many=True, ).data)

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    renderer_classes = [renderers.JSONRenderer]

    def get_queryset(self):
        return Subject.objects.all()  

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    renderer_classes = [renderers.JSONRenderer]
    def get_queryset(self):
        return Choice.objects.all()

class TeacherViewSet(viewsets.ModelViewSet):
    queryset =  Teacher.objects.all()
    serializer_class = TeacherSerializer
    renderer_classes = [renderers.JSONRenderer]

    @action(detail=True, url_path="subjects", methods=['GET'])
    def subjects(self, *args, **kwargs):
        current_teacher = self.get_object()
        subjects = Subject.objects.filter(teacher=current_teacher)
        
        serializer = SubjectSerializer(subjects, many=True)
        data = serializer.data

        return Response({
           "subjects": data, 
        })