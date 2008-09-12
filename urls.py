from django.conf.urls.defaults import *
from django.conf import settings
from prelimbook.examlog import models
import re

from django.contrib import admin
admin.autodiscover()

#urlb = r"^%s" % re.escape(settings.DYNSITE_ROOT.lstrip("/"))
urlb = "^"

urlpatterns = patterns('',
        (urlb+r'login/$', 'django.contrib.auth.views.login',
            ),
        (urlb+r'logout/$', 'django.contrib.auth.views.logout',
            ),

        (urlb+r'$', 'django.views.generic.simple.direct_to_template',
            {
            "template": "base.html"
            }),

        (urlb+r'by_prof/$', 'prelimbook.examlog.views.object_list',
            {
            "queryset": models.Professor.objects.all(),
            "paginate_by": 30
            }),
        (urlb+r'by_prof/(?P<prof_id>[0-9]+)/$',
                'prelimbook.examlog.views.by_professor'),

        (urlb+r'by_class/$', 'prelimbook.examlog.views.object_list',
            {
            "queryset": models.Lecture.objects.all(),
            "paginate_by": 30
            }),
        (urlb+r'by_class/(?P<class_id>[0-9]+)/$',
                'prelimbook.examlog.views.by_class'),

        (urlb+r'by_student/$', 'prelimbook.examlog.views.object_list',
            {
            "template_name": "examlog/student_list.html",
            "queryset": models.ExamReport.objects.all(),
            "paginate_by": 30
            }),
        (urlb+r'by_student/(?P<report_id>[0-9]+)/$',
                'prelimbook.examlog.views.by_student'),

        (urlb+r'by_year/$', 'prelimbook.examlog.views.object_list',
            {
            "template_name": "examlog/year_list.html",
            "queryset": models.ExamReport.objects.values("year").order_by("year").distinct(),
            }),
        (urlb+r'by_year/(?P<year>[0-9]+)/$',
                'prelimbook.examlog.views.by_year'),

        (urlb+r'admin/(.*)', admin.site.root),
)
