"""lessons URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from marks.api import ChoiceViewSet, JournalViewSet, LessonViewSet, SchoolViewSet, StudentViewSet, SubjectViewSet, TeacherViewSet
import marks.urls
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(r'students', StudentViewSet, basename='student')
router.register(r'schools', SchoolViewSet, basename='school')
router.register(r'teachers', TeacherViewSet, basename='teacher')
router.register(r'journals', JournalViewSet, basename='journal')
router.register(r'lessons', LessonViewSet, basename='lesson')
router.register(r'choices', ChoiceViewSet, basename='choice')
router.register(r'subjects', SubjectViewSet, basename='subject')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/marks/', include(marks.urls)),
    path("api/", include(router.urls)),
]
