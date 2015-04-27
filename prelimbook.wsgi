import os, sys
sys.path.append("/webapp/prelimbook")
os.environ['DJANGO_SETTINGS_MODULE'] = 'prelimbook.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
