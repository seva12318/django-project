from gc import get_objects
from msilib.schema import Class
from rest_framework import viewsets, renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from marks.models import Choice, Journal, Lesson, School, Student, Subject, Teacher
from marks.serializer import JournalReportSerializer, ChoiceSerializer, JournalSerializer, LessonAddMarkSerializer, LessonSerializer, SchoolAddStudentsSerializer, SchoolSerializer, StudentSerializer, SubjectSerializer, TeacherSerializer

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
    def lesson(self, *args, **kwargs):
        journal = Journal.objects.filter(students=self.kwargs['pk'])
        serializer = JournalSerializer(journal, many=True)
        data = serializer.data

        return Response({
            "journal": data,
        })  
    
    @action(detail=True, url_path="school", methods=['GET'])
    def school(self, *args, **kwargs):
        participants = Student.objects.filter(school=self.kwargs['pk'])
        #serializer = StudentSerializer(participants, many=True)
        i=0
        for part in participants:
            journal = Journal.objects.filter(students = part)
            serializer = JournalReportSerializer(journal, many=True)
            #КОСТЫЛЬ, НО НАДЕЮСЬ, ЧТО ПЕРЕДЕЛАЮ 
            if i == 0:
                data = serializer.data
            else:
                data=data+serializer.data
            i=i+1

        return Response({
            "school-journal": data,
        })

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    renderer_classes = [renderers.JSONRenderer]

    def get_queryset(self):
        return Lesson.objects.all()  

    @action(detail=True, url_path="journal", methods=['GET'])
    def journal(self, *args, **kwargs):
        current_lesson = self.get_object()
        journal = Journal.objects.filter(lessons = current_lesson)
        serializer = JournalSerializer(journal, many=True)
        data = serializer.data

        return Response({
            "journal" : data
        })

    @action(detail=True, url_path="get-marks", methods=['POST'])
    def get_marks(self,request, *args, **kwargs):
        current_lesson = self.get_object()
        serializer = LessonAddMarkSerializer(data=request.data)
        if serializer.is_valid(True):
            #serializer.save()   
            if  Journal.objects.filter(students_id = request.data['students'], lessons_id = request.data['lessons']).count()==0:
                Journal.objects.create(students_id = request.data['students'], lessons_id = request.data['lessons'] ,mark=request.data['mark'])
            else:
                Journal.objects.filter(students_id = request.data['students'], lessons_id = request.data['lessons']).update(mark = request.data['mark'])
            return Response(status=200)
        else:
    	    return Response(status=400)

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