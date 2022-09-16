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
from django.conf import settings
from marks.api import ChoiceViewSet, JournalViewSet, LessonViewSet, SchoolViewSet, StudentViewSet, SubjectViewSet, TeacherViewSet
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
    #path('api/marks/', include(marks.urls)),
    path("api/", include(router.urls)),
    path('accounts/',  include('django.contrib.auth.urls')),
    
    #path('register/', user_views.register, name = 'register'),
    #path('profile/', user_views.profile, name = 'profile'),
    path('home/', include('marks.urls')),
    #path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name = 'logout'),
    #path('password-reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'), name = 'password_reset'),
    #path('password-reset/done/', auth_views.PasswordResetView.as_view(template_name='account/password_reset_done.html'), name = 'password_reset_done'),
    #path('password-reset-confirm/<uidb64>/token/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'), name = 'password_reset_confirm'),
    #path('password-reset-complete/', auth_views.PasswordCompleteView.as_view(template_name='account/password_reset_complete.html'), name = 'password_reset_complete'),


]
