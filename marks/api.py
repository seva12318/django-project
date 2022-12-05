from rest_framework import viewsets, renderers
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from marks.models import Choice, Journal, Lesson, School, Student, Subject, Teacher
from marks.permissions import IsStaffUser
from marks.serializer import IdUserSerializer, JournalReportSerializer, JournalSerializer, \
    LessonAddMarkSerializer, LessonSerializer, SchoolSerializer, StudentSerializer, \
    SubjectSerializer, TeacherSerializer


###########ДЛЯ ПОЛЬЗОВАТЕЛЯ######################

class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    renderer_classes = [renderers.JSONRenderer]
    permission_classes = [IsStaffUser]

    def get_queryset(self):
        return Journal.objects.filter(
            lessons__subjects__teacher__in=Teacher.objects.filter(user=self.request.user.id)
        ).all()

    #########################ОЦЕНКИ КОНКРЕТНОГО СТУДЕНТА(ВСЕ ПРЕДМЕТЫ)###############################
    @action(detail=True, url_path="lesson", methods=['GET'])
    def lesson(self, *args, **kwargs):
        journal = Journal.objects.filter(students=self.kwargs['pk'])
        serializer = JournalSerializer(journal, many=True)
        data = serializer.data

        return Response({
            "journal": data,
        })

    #####################ОЦЕНКИ СТУДЕНТОВ С ФИЛЬТРОМ ПО ШКОЛАМ(ОТЧЕТ)##################################
    @action(detail=True, url_path="school", methods=['GET'])
    def school(self, *args, **kwargs):
        participants = Student.objects.filter(school=self.kwargs['pk'])
        data = []
        for part in participants:
            journal = Journal.objects.filter(students=part)
            serializer = JournalReportSerializer(journal, many=True)
            # КОСТЫЛЬ, НО НАДЕЮСЬ, ЧТО ПЕРЕДЕЛАЮ
            data = data + serializer.data

        return Response({
            "school-journal": data,
        })

    #####################ОЦЕНКИ СТУДЕНТОВ С ФИЛЬТРОМ ПО ПРЕДМЕТУ(ОТЧЕТ)##################################
    @action(detail=True, url_path="subject", methods=['GET'])
    def subject(self, *args, **kwargs):
        data = None
        param1 = Choice.objects.filter(sub_first=self.kwargs['pk'])
        param2 = Choice.objects.filter(sub_second=self.kwargs['pk'])
        if param1.count() > 0 and param2.count() > 0:
            data = students_data(param1, self.kwargs['pk']) + students_data(param2, self.kwargs['pk'])
        elif param1.count() > 0 and param2.count() == 0:
            data = students_data(param1, self.kwargs['pk'])
        elif param1.count() == 0 and param2.count() > 0:
            data = students_data(param2, self.kwargs['pk'])

        return Response({
            "sub-journal": data,
        })   


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    renderer_classes = [renderers.JSONRenderer]
    permission_classes = [IsStaffUser]

    ######################ОЦЕНКИ ЗА КОНКРЕТНЫЙ УРОК#####################################
    @action(detail=True, url_path="journal", methods=['GET'])
    def journal(self, *args, **kwargs):
        current_lesson = self.get_object()
        subjects = Lesson.objects.filter(subjects__in=Subject.objects.filter(
            teacher__in=Teacher.objects.filter(user=self.request.user.id))
        )
        i = 0
        for sub in subjects.values('id'):
            if sub['id'] == current_lesson.id:
                i = 1
                break
        if i == 0:
            return Response(status=400)

        journal = Journal.objects.filter(lessons=current_lesson)
        serializer = JournalSerializer(journal, many=True)
        data = serializer.data
        return Response({
            "journal": data
        })

    ###############################ПРОСТАВЛЕНИЕ ОЦЕНОК########################################
    @action(detail=True, url_path="get-marks", methods=['POST'])
    def get_marks(self, request, *args, **kwargs):
        current_lesson = self.get_object()
        serializer = LessonAddMarkSerializer(data=request.data)
        if serializer.is_valid(True):
            # serializer.save()
            if Journal.objects.filter(students_id=request.data['students'],
                                      lessons_id=request.data['lessons']).count() == 0:
                Journal.objects.create(students_id=request.data['students'], lessons_id=request.data['lessons'],
                                       mark=request.data['mark'])
            else:
                Journal.objects.filter(students_id=request.data['students'], lessons_id=request.data['lessons']).update(
                    mark=request.data['mark'])
            return Response(status=200)
        else:
            return Response(status=400)


class SubjectViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Subject.objects.filter(teacher__user=self.request.user.id)

    serializer_class = SubjectSerializer
    renderer_classes = [renderers.JSONRenderer]
    permission_classes = [IsStaffUser]

    ################################ДОМАШКИ И ТЕМЫ УРОКОВ ПО ПРЕДМЕТУ################################################
    @action(detail=True, url_path="lessons", methods=['GET'])
    def lessons(self, *args, **kwargs):
        current_sub = self.get_object()
        # teacher = Teacher.objects.get(user=self.request.user)
        lessons = Lesson.objects.filter(subjects_id=current_sub, subjects__teacher__user=self.request.user)
        serializer = LessonSerializer(lessons, many=True)
        data = serializer.data

        return Response({
            "sub-lessons": data,
        })

    #################################СПИСОК СТУДЕНТОВ ПО ПРЕДМЕТУ##################################################
    @action(detail=True, url_path="students", methods=['GET'])
    def students(self, *args, **kwargs):
        data = None
        param1 = Choice.objects.filter(sub_first=self.kwargs['pk'])
        param2 = Choice.objects.filter(sub_second=self.kwargs['pk'])
        if param1.count() > 0 and param2.count() > 0:
            data = students_list(param1) + students_list(param2)
        elif param1.count() > 0 and param2.count() == 0:
            data = students_list(param1)
        elif param1.count() == 0 and param2.count() > 0:
            data = students_list(param2)

        return Response({
            "sub-journal": data,
        })


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    renderer_classes = [renderers.JSONRenderer]
    permission_classes = [IsStaffUser]

    def get_current_teacher(self):
        return Teacher.objects.get(user=self.request.user.id)

    ###########################ПРЕДМЕТЫ, КОТОРЫЕ ВЕДЕТ УЧИТЕЛЬ##############################
    @action(detail=False, url_path="subjects", methods=['GET'])
    def subjects(self, *args, **kwargs):
        current_teacher = self.get_current_teacher()
        subjects = Subject.objects.filter(teacher=current_teacher)

        serializer = SubjectSerializer(subjects, many=True)
        data = serializer.data

        return Response({
            "subjects": data,
        })

    ###########################id　авторизоавнного учителя###################################
    @action(detail=False, url_path="user", methods=['GET'])
    def user(self, *args, **kwargs):
        current_teacher = self.request.user.id
        teacher = Teacher.objects.filter(user=current_teacher)
        serializer = IdUserSerializer(teacher, many=True)
        data = serializer.data
        return Response({
            "teacher": data,
        })


class ActiveTeacherViewSet(viewsets.GenericViewSet):
    renderer_classes = [renderers.JSONRenderer]
    permission_classes = [IsAuthenticated]

    def get_current_teacher(self):
        return Teacher.objects.get(user=self.request.user)

    ########ПРЕДМЕТЫ АВТОРИЗОВАННОГО УЧИТЕЛЯ##########################
    @action(detail=False, url_path="subjects", methods=['GET'])
    def subjects(self, *args, **kwargs):
        current_teacher = self.get_current_teacher()
        subjects = Subject.objects.filter(teacher=current_teacher)

        serializer = SubjectSerializer(subjects, many=True)
        data = serializer.data

        return Response({
            "subjects": data,
        })


def students_data(participants, sub_id):
    data = []
    for part in participants:
        lesson = Lesson.objects.filter(subjects_id=sub_id)
        for less in lesson:
            journal = Journal.objects.filter(students=part.students, lessons=less)
            serializer = JournalReportSerializer(journal, many=True)
            data = data + serializer.data
    return data


def students_list(participants):
    data = []
    for part in participants:
        students = Student.objects.filter(id=part.students.id)
        serializer = StudentSerializer(students, many=True)
        data = data + serializer.data
    return data


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    renderer_classes = [renderers.JSONRenderer]
    permission_classes = [IsStaffUser]
