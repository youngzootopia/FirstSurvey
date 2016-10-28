"""
WSGI config for survey project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/root/first/survey/survey/lib/python3.4/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/root/first/survey/survey')
sys.path.append('/root/first/survey/first')
sys.path.append('/root/first/survey/first/static')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "survey.settings")

# Activate your virtual env
activate_env="/root/first/survey/survey/bin/activate_this.py"
execfile(activate_env, dict(__file__=activate_env))

application = get_wsgi_application()
