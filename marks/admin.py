from django.contrib import admin

from marks.models import Choice, Journal, Lesson, School, Student, Subject, Teacher

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    pass

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    pass
