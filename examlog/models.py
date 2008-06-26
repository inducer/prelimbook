from django.db import models

class Professor(models.Model):
    first_name = models.CharField(maxlength=200)
    last_name = models.CharField(maxlength=200)

    class Meta:
        ordering = ("last_name", )

    class Admin:
        pass
    
    def __str__(self):
        return "%s, %s" % (self.last_name, self.first_name)

class Discipline(models.Model):
    code = models.CharField(maxlength=2)
    name = models.CharField(maxlength=100)

    class Admin:
        pass
    
    def __str__(self):
        return self.code

class Lecture(models.Model):
    discipline = models.ForeignKey(Discipline)
    number = models.CharField(maxlength=6)
    name = models.CharField(maxlength=200)

    class Admin:
        pass

    class Meta:
        ordering = ("number",)
    
    def __str__(self):
        return "%s%s (%s)" % (self.discipline, self.number, self.name)


class ExamType(models.Model):
    name = models.CharField(maxlength=100)

    class Admin:
        pass
    
    def __str__(self):
        return self.name

class ExamReport(models.Model):
    student_first_name = models.CharField(maxlength=100, blank=True)
    student_last_name = models.CharField(maxlength=100, blank=True)
    year = models.IntegerField(blank=True, null=True)
    chair = models.ForeignKey(Professor, core=True, null=True, blank=True)
    report = models.FileField("complete report",
            blank=True, upload_to="report_files",
            help_text="Please upload PDF files only.")

    class Meta:
        ordering = ['student_last_name']

    class Admin:
        list_filter = ('year',)
        list_display = ('id', 'year', 'student_first_name', 
                'student_last_name')

    def __str__(self):
        first_name = self.student_first_name
        last_name = self.student_last_name
        if not (first_name or last_name):
            name = None
        elif last_name:
            if first_name:
                name = "%s %s" % (first_name, last_name)
            else:
                name = last_name
        else:
            name = first_name

        if self.year and name:
            return "%s (%d)" % (name, self.year)
        elif name:
            return name
        elif self.year:
            return "[No name] (%d)" % self.year
        else:
            return "Report number %d" % self.id

class ExamSubject(models.Model):
    report = models.ForeignKey(ExamReport, edit_inline=True,
            num_in_admin=8, num_extra_on_change=6)
    examiner = models.ForeignKey(Professor, core=True)
    lecture = models.ForeignKey(Lecture, core=True)
    exam_type = models.ForeignKey(ExamType)
    subject_report = models.FileField(blank=True, upload_to="subjrep_files",
           help_text="Please upload PDF files only.", null=True)
    remarks = models.CharField(maxlength=100, blank=True, null=True)

    #class Admin:
        #pass

