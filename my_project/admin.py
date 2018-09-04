from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Student, Teacher, Class, Question, Answer



class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'avg_mark')
    search_fields = ('id', 'first_name')
    ordering = ('first_name',)
    list_display_links = list_display


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'subject')
    search_fields = ('id', 'first_name')
    ordering = ('first_name',)
    list_display_links = list_display


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Class)
admin.site.register(Question)
admin.site.register(Answer)
