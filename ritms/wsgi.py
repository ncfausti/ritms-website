"""
WSGI config for ritms project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

import sys
import site

site.addsitedir('/home/ec2-user/.virtualenvs/ritms/lib/python2.7/site-packages')

#root_path = os.path.abspath(os.path.split(__file__)[0])
#sys.path.insert(0, os.path.join(root_path, 'ritms'))
#sys.path.insert(0, root_path)
sys.path.insert(0,"../")
sys.path.insert(0,"../../")
sys.path.append("/var/www/ritms")
sys.path.append("/var/www/ritms/ritms")

activate_env=os.path.expanduser('/home/ec2-user/.virtualenvs/ritms/bin/activate_this.py')
execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

application = get_wsgi_application()
