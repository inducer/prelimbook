from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from prelimbook.examlog.models import ExamReport, Lecture, Professor



from django.views.generic.list_detail import object_list
# decorators ------------------------------------------------------------------
login_required = user_passes_test(lambda u: u.is_authenticated(),
        login_url = settings.DYNSITE_ROOT+"login/")




# generic view ----------------------------------------------------------------
object_list = login_required(object_list)




# detailed views --------------------------------------------------------------
def list_reports(request, object_list):
    return render_to_response(
            "examlog/examreport_list.html",
            {"object_list": object_list},
            context_instance=RequestContext(request)
            )

def by_student(request, report_id):
    return list_reports(request, ExamReport.objects.filter(id=report_id))

def by_year(request, year):
    return list_reports(request, ExamReport.objects.filter(year=year))

def by_class(request, class_id):
    reports = [
    ExamReport.objects.get(id=obj["report"])
    for obj in Lecture.objects.get(id=class_id).examsubject_set\
            .values("report").distinct()]
    return list_reports(request, reports)

def by_professor(request, prof_id):
    reports = [
    ExamReport.objects.get(id=obj["report"])
    for obj in Professor.objects.get(id=prof_id).examsubject_set\
            .values("report").distinct()]
    return list_reports(request, reports)
