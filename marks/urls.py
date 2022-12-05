#from xml.etree.ElementInclude import include
from django.db import router
from marks.views import ChoicesView, LessonView, OneLessonView, OneSchoolView, OneStudentView, OneSubjectView, OneTeacherView, SchoolView, StudentView, SubjectView, TeacherView
from django.urls import include, path
from marks import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


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
    path("choices/", ChoicesView.as_view()),
    path('', views.home, name = 'home'),
    path("signup/", views.SignUp.as_view(), name="signup"),
]
