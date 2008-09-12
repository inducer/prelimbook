from django.db import models

class Professor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    class Meta:
        ordering = ("last_name", )

    def __unicode__(self):
        return u"%s, %s" % (self.last_name, self.first_name)

class Discipline(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.code

class Lecture(models.Model):
    discipline = models.ForeignKey(Discipline)
    number = models.CharField(max_length=20)
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ("number",)
    
    def __unicode__(self):
        return u"%s%s (%s)" % (self.discipline, self.number, self.name)


class ExamType(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class ExamReport(models.Model):
    student_first_name = models.CharField(max_length=100, blank=True)
    student_last_name = models.CharField(max_length=100, blank=True)
    year = models.IntegerField(blank=True, null=True)
    chair = models.ForeignKey(Professor, null=True, blank=True)
    report = models.FileField(u"complete report",
            blank=True, upload_to="report_files",
            help_text=u"Please upload PDF files only.")

    class Meta:
        ordering = ['student_last_name']

    def __unicode__(self):
        first_name = self.student_first_name
        last_name = self.student_last_name
        if not (first_name or last_name):
            name = None
        elif last_name:
            if first_name:
                name = u"%s %s" % (first_name, last_name)
            else:
                name = last_name
        else:
            name = first_name

        if self.year and name:
            return u"%s (%d)" % (name, self.year)
        elif name:
            return name
        elif self.year:
            return u"[No name] (%d)" % self.year
        else:
            return u"Report number %d" % self.id

class ExamSubject(models.Model):
    report = models.ForeignKey(ExamReport)
    examiner = models.ForeignKey(Professor)
    lecture = models.ForeignKey(Lecture)
    exam_type = models.ForeignKey(ExamType)
    subject_report = models.FileField(blank=True, upload_to="subjrep_files",
           help_text="Please upload PDF files only.", null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)
