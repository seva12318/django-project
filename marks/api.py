from gc import get_objects
from msilib.schema import Class
from rest_framework import viewsets, renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from marks.models import School, Student
from marks.serializer import SchoolAddStudentsSerializer, SchoolSerializer, StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset =  Student.objects.all()
    serializer_class = StudentSerializer
    renderer_classes = [renderers.JSONRenderer]

    def get_queryset(self):
        #self.request.user
        return Student.objects.all()

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