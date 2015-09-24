import os, sys
sys.path.append('/home/dedo/Django/inventory/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'inventory.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()