import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'image_uploader.settings')

try:
    application = get_wsgi_application()
except Exception as e:
    sys.exit(1)
