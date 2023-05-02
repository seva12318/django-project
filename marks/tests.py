import json

from model_bakery import baker
from django.test import Client, TestCase
from django.contrib.auth.models import User

from marks.models import Teacher, Student, School, Subject, Lesson, Journal


class Setup(TestCase):
    def setUp(self):
        self.admin = baker.make(User, is_superuser=True)
        self.users = [
            baker.make(User, is_staff=True),
            baker.make(User, is_staff=True)
        ]
        self.client = Client()
        self.teachers = []
        self.schools = []
        self.students = []
        self.subjects = []
        self.lessons = []
        self.journal = []


def definition(self, teacher=None, school=None, student=None, subject=None, lesson=None, journal=None, all=None):
    if all:
        teacher, school, student, subject, lesson, journal = [True for i in range(6)]
    if teacher:
        self.teachers = [
            baker.make(Teacher, surname='Фам1', name='Имя1', patr='Отч1', user=self.users[0]),
            baker.make(Teacher, surname='Фам2', name='Имя2', patr='Отч2', user=self.users[1])
        ]
    if school:
        self.schools = [
            baker.make(School, title='Школа1'),
            baker.make(School, title='Школа2')
        ]
    if student:
        self.students = [
            baker.make(Student, surname='СтФам1', name='СтИмя1', patr='СтОтч1', school=self.schools[0], num_class='10а'),
            baker.make(Student, surname='СтФам2', name='СтИмя2', patr='СтОтч2', school=self.schools[0], num_class='10б'),
            baker.make(Student, surname='СтФам3', name='СтИмя3', patr='СтОтч3', school=self.schools[1], num_class='10в'),
            baker.make(Student, surname='СтФам4', name='СтИмя4', patr='СтОтч4', school=self.schools[1], num_class='10г'),
        ]
    if subject:
        self.subjects = [
            baker.make(Subject, level='1', name='Предм1', time='00:00', teacher=self.teachers[0]),
            baker.make(Subject, level='2', name='Предм2', time='10:00', teacher=self.teachers[1])
        ]
    if lesson:
        self.lessons = [
            baker.make(Lesson, subjects=self.subjects[0], topic='Тема1', homework='ДЗ1', date='01.01.2020'),
            baker.make(Lesson, subjects=self.subjects[1], topic='Тема2', homework='ДЗ2', date='02.01.2020')
        ]
    if journal:
        self.journal = [
            baker.make(Journal, students=self.students[0], lessons=self.lessons[0], mark='4'),
            baker.make(Journal, students=self.students[1], lessons=self.lessons[0], mark='3'),
            baker.make(Journal, students=self.students[2], lessons=self.lessons[1], mark='2'),
            baker.make(Journal, students=self.students[3], lessons=self.lessons[1], mark='5')
        ]


class TestTeachersApi(Setup):
    def test_get_teachers_list(self):
        self.client.force_login(self.users[0])
        definition(self, teacher=True)
        resp_list = self.client.get("/api/teachers/").json()
        for teacher in self.teachers:
            self.assertEqual(teacher.surname, resp_list[self.teachers.index(teacher)]['surname'])
            self.assertEqual(teacher.name, resp_list[self.teachers.index(teacher)]['name'])
            self.assertEqual(teacher.patr, resp_list[self.teachers.index(teacher)]['patr'])
        self.client.logout()

    def test_teachers_subjects(self):
        self.client.force_login(self.users[0])
        definition(self, teacher=True, subject=True)
        resp = self.client.get("/api/teachers/subjects/").json()
        for resp_subject in resp['subjects']:
            for subject in self.subjects:
                if subject.teacher == self.teachers[0]:
                    self.assertEqual(resp_subject['id'], subject.id)
        self.client.logout()

    def test_id(self):
        self.client.force_login(self.users[1])
        definition(self, teacher=True)
        self.assertEqual(self.client.get("/api/teachers/user/").json()['teacher'][0]['id'],self.teachers[1].id)
        self.client.logout()

class TestSchoolApi(Setup):
    def test_get_schools_list(self):
        self.client.force_login(self.users[0])
        definition(self, school=True)
        resp_list = self.client.get("/api/schools/").json()
        for school in self.schools:
            self.assertEqual(school.title, resp_list[self.schools.index(school)]['title'])
        self.client.logout()

class TestLessonsApi(Setup):
    def test_get_lessons_list(self):
        self.client.force_login(self.users[0])
        definition(self, lesson=True, subject=True, teacher=True)
        resp_list = self.client.get("/api/lessons/").json()
        for lesson in self.lessons:
            self.assertEqual(lesson.id, resp_list[self.lessons.index(lesson)]['id'])
            self.assertEqual(lesson.subjects.id, resp_list[self.lessons.index(lesson)]['subjects'])
            self.assertEqual(lesson.subjects.__str__(), resp_list[self.lessons.index(lesson)]['subjects_name'])
            self.assertEqual(lesson.topic, resp_list[self.lessons.index(lesson)]['topic'])
            self.assertEqual(lesson.homework, resp_list[self.lessons.index(lesson)]['homework'])
            self.assertEqual(lesson.date, resp_list[self.lessons.index(lesson)]['date'])
        self.client.logout()

    def test_get_marks_by_lesson(self):
        self.client.force_login(self.users[0])
        definition(self, all=True)
        resp_list = self.client.get("/api/lessons/7/journal/").json()
        for resp_mark in resp_list['journal']:
            for mark in self.journal:
                if mark.id == resp_mark['id']:
                    self.assertEqual(mark.students.id, resp_mark['students'])
                    self.assertEqual(mark.students.__str__(), resp_mark['students_name'])
                    self.assertEqual(mark.lessons.id, resp_mark['lessons'])
                    self.assertEqual(mark.mark, resp_mark['mark'])
        self.client.logout()

    def test_post_mark(self):
        self.client.force_login(self.users[0])
        definition(self, all=True)
        test_len = Journal.objects.count()
        self.assertEqual(self.client.post("/api/lessons/9/get-marks/", json.dumps({'students':13,'mark':'2'}), content_type='application/json').status_code, 200)
        self.assertEqual(test_len, Journal.objects.count())

class TestJournalApi(Setup):
    def test_get_journal_by_teacher(self):
        self.client.force_login(self.users[0])
        definition(self, all=True)
        resp_list = self.client.get("/api/journals/").json()
        valid_journal = []
        for i in range(len(self.journal)):
            if self.journal[i].lessons.subjects.teacher.user.id == self.users[0].id:
                valid_journal.append(self.journal[i])
        self.assertEqual(len(resp_list), len(valid_journal))
        for resp_mark in resp_list:
            for mark in self.journal:
                if mark.id == resp_mark['id']:
                    self.assertEqual(resp_mark['students'], mark.students.id)
                    self.assertEqual(resp_mark['students_name'], mark.students.__str__())
                    self.assertEqual(resp_mark['lessons'], mark.lessons.id)
                    self.assertEqual(resp_mark['mark'], mark.mark)
        self.client.logout()

    def test_get_journal_by_student(self):
        self.client.force_login(self.users[0])
        definition(self, all=True)
        resp_list = self.client.get("/api/journals/5/lesson/").json()
        valid_journal = []
        for i in range(len(self.journal)):
            if self.journal[i].students.id == 5:
                valid_journal.append(self.journal[i])
        self.assertEqual(len(resp_list['journal']), len(valid_journal))
        for resp_mark in resp_list['journal']:
            for mark in valid_journal:
                if resp_mark['id'] == mark.id:
                    self.assertEqual(resp_mark['students'], mark.students.id)
                    self.assertEqual(resp_mark['students_name'], mark.students.__str__())
                    self.assertEqual(resp_mark['lessons'], mark.lessons.id)
                    self.assertEqual(resp_mark['mark'], mark.mark)
        self.client.logout()

    # def test_get_journal_by_school(self):
    #     self.client.force_login(self.users[0])
    #     definition(self, all=True)
    #     resp_list = self.client.get("/api/journals/1/school/").json()
    #     valid_journal = []
    #     for mark in self.journal:
    #         if mark.students.school.id == 1:
    #             valid_journal.append(mark)
    #     self.assertEqual(len(resp_list['school-journal']), len(valid_journal))
    #     for resp_mark in resp_list['school-journal']:
    #         for mark in valid_journal:
    #             if resp_mark['id'] == mark.id:
    #                 self.assertEqual(resp_mark['students'], mark.students.id)
    #                 self.assertEqual(resp_mark['students_name'], mark.students.__str__())
    #                 self.assertEqual(resp_mark['num_class'], mark.students.num_class)
    #                 self.assertEqual(resp_mark['lessons'], mark.lessons.id)
    #                 self.assertEqual(resp_mark['date'], mark.lessons.date)
    #                 self.assertEqual(resp_mark['lessons_name'], mark.lessons.__str__())
    #                 self.assertEqual(resp_mark['mark'], mark.mark)
    #     self.client.logout()

    # def test_get_journal_by_subject(self):
    #     self.client.force_login(self.users[0])
    #     definition(self, all=True)
    #     resp_list = self.client.get("/api/journals/1/school/").json()
    #     valid_journal = []
    #     for mark in self.journal:
    #         if mark.subjects.id == 1:
    #             valid_journal.append(mark)
    #     self.assertEqual(len(resp_list['sub-journal']), len(valid_journal))
    #     for resp_mark in resp_list['sub-journal']:
    #         for mark in valid_journal:
    #             if resp_mark['id'] == mark.id:
    #                 self.assertEqual(resp_mark['students'], mark.students.id)
    #                 self.assertEqual(resp_mark['students_name'], mark.students.__str__())
    #                 self.assertEqual(resp_mark['num_class'], mark.students.num_class)
    #                 self.assertEqual(resp_mark['lessons'], mark.lessons.id)
    #                 self.assertEqual(resp_mark['date'], mark.lessons.date)
    #                 self.assertEqual(resp_mark['lessons_name'], mark.lessons.__str__())
    #                 self.assertEqual(resp_mark['mark'], mark.mark)
    #     self.client.logout()

class TestSubjectApi(Setup):
    def test_get_subject_list(self):
        self.client.force_login(self.users[0])
        definition(self, teacher=True, lesson=True, subject=True)
        resp_list = self.client.get("/api/subjects/").json()
        valid_list = []
        for subject in self.subjects:
            if subject.teacher.user.id == self.users[0].id:
                valid_list.append(subject)
        self.assertEqual(len(resp_list),len(valid_list))
        for resp_subject in resp_list:
            for subject in valid_list:
                if resp_subject['id'] == subject.id:
                    self.assertEqual(resp_subject['level'], subject.level)
                    self.assertEqual(resp_subject['name'], subject.name)
                    self.assertEqual(resp_subject['time'], subject.time)
                    self.assertEqual(resp_subject['teacher'], subject.teacher.id)
                    self.assertEqual(resp_subject['teacher_fio'], subject.teacher.__str__())
        self.client.logout()

    def test_get_lessons_by_teacher(self):
        self.client.force_login(self.users[0])
        definition(self, teacher=True, lesson=True, subject=True)
        resp_list = self.client.get("/api/subjects/11/lessons/").json()
        valid_list = []
        for lesson in self.lessons:
            if lesson.subjects.teacher.user.id == self.users[0].id:
                valid_list.append(lesson)
        self.assertEqual(len(resp_list), len(valid_list))
        for resp_lesson in resp_list['sub-lessons']:
            for lesson in valid_list:
                if resp_lesson['id'] == lesson.id:
                    self.assertEqual(resp_lesson['subjects'], lesson.subjects.id)
                    self.assertEqual(resp_lesson['subjects_name'], lesson.subjects.__str__())
                    self.assertEqual(resp_lesson['topic'], lesson.topic)
                    self.assertEqual(resp_lesson['homework'], lesson.homework)
                    self.assertEqual(resp_lesson['date'], lesson.date)
        self.client.logout()
