from marks.views import LessonView, OneLessonView, OneSchoolView, OneStudentView, OneSubjectView, OneTeacherView, SchoolView, StudentView, SubjectView, TeacherView
from django.urls import path

urlpatterns = [
    path("students/", StudentView.as_view()),
    path("students/<int:id>/", OneStudentView.as_view()),
    path("school/", SchoolView.as_view()),
    path("school/<int:id>/", OneSchoolView.as_view()),
    path("teachers/", TeacherView.as_view()),
    path("teachers/<int:id>/", OneTeacherView.as_view()),
    path("subjects/", SubjectView.as_view()),
    path("subjects/<int:id>/", OneSubjectView.as_view()),
    path("lessons/", LessonView.as_view()),
    path("lessons/<int:id>/", OneLessonView.as_view()),
]
