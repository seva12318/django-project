from django.contrib import admin

from marks.models import Choice, Journal, Lesson, School, Student, Subject, Teacher

# Register your models here
admin.site.register(Student)
#class StudentAdmin(admin.ModelAdmin):
#    pass

admin.site.register(School)
#class SchoolAdmin(admin.ModelAdmin):
#    pass

admin.site.register(Teacher)
#class TeacherAdmin(admin.ModelAdmin):
#    pass

admin.site.register(Subject)
#class SubjectAdmin(admin.ModelAdmin):
#    pass

admin.site.register(Lesson)
#class LessonAdmin(admin.ModelAdmin):
#    pass

admin.site.register(Journal)
#class JournalAdmin(admin.ModelAdmin):
#    pass

admin.site.register(Choice)
#class ChoiceAdmin(admin.ModelAdmin):
#    pass
