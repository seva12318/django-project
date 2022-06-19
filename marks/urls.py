from marks.views import OneStudentView, StudentView
from django.urls import path

urlpatterns = [
    path("students/", StudentView.as_view()),
    path("students/<int:id>/", OneStudentView.as_view())
]
