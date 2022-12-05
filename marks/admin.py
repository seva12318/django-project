from django.contrib import admin

from marks.models import Choice, Journal, Lesson, School, Student, Subject, Teacher

# Register your models here
class StudentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'school', 'num_class')
    list_display_links = ('__str__',)
    list_editable = ('school',)
    search_fields = ('name','surname', 'patr','school__title')
admin.site.register(Student,StudentAdmin)

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)
admin.site.register(School, SchoolAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('__str__','user')
    list_display_links = ('__str__',)
    list_editable = ('user',)
    search_fields = ('name','surname', 'patr','user__username')
admin.site.register(Teacher, TeacherAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name','teacher','level','time',)
    list_display_links = ('name', )
    list_editable = ('level','time','teacher')
    search_fields = ('name','teacher__name')

admin.site.register(Subject, SubjectAdmin)

class LessonAdmin(admin.ModelAdmin):
    list_display = ('subjects','date','topic', 'homework')
    list_display_links = ('subjects',)
    search_fields = ('subjects__name','date','topic')
admin.site.register(Lesson,LessonAdmin)


class JournalAdmin(admin.ModelAdmin):
    list_display = ('students','lessons', 'mark')
    list_display_links = ('students','lessons')
    search_fields = ('students__name','students__surname', 'students__patr','lessons__topic')

admin.site.register(Journal, JournalAdmin)

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('students','sub_first','sub_second')
    list_display_links = ('students',)
    list_editable = ('sub_first','sub_second')
    search_fields = ('students__name','students__surname', 'students__patr','sub_first__name','sub_second__name')

admin.site.register(Choice, ChoiceAdmin)

