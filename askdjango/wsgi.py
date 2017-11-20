"""
WSGI config for askdjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# DJANGO_SETTINGS_MODULE을 지정하지 않았을 때 DEFAULT값으로 두번째 인자인 askdjango.settings.prod 실행된다.
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "askdjango.settings") #settings분기전
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "askdjango.settings.prod") #settings분기후 #manage.py는 주로 개발에 사용하여 .dev로 셋팅 #wsgi.py는 서비스 배포때만 씀

application = get_wsgi_application()
