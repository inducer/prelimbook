from django.contrib import admin
from models import \
        Professor, \
        Discipline, \
        Lecture, \
        ExamType, \
        ExamReport, \
        ExamSubject

class ProfessorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Professor, ProfessorAdmin)

class DisciplineAdmin(admin.ModelAdmin):
    pass

admin.site.register(Discipline, DisciplineAdmin)

class LectureAdmin(admin.ModelAdmin):
    pass

admin.site.register(Lecture, LectureAdmin)

class ExamTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(ExamType, ExamTypeAdmin)

class ExamSubjectInline(admin.TabularInline):
    model = ExamSubject
    extra = 8

class ExamReportAdmin(admin.ModelAdmin):
    list_filter = ('year',)
    list_display = ('id', 'year', 'student_first_name', 
            'student_last_name')

    inlines = [ExamSubjectInline]

admin.site.register(ExamReport, ExamReportAdmin)
