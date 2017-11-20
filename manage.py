#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # DJANGO_SETTINGS_MODULE을 지정하지 않았을 때 DEFAULT값으로 두번째 인자인 askdjango.settings.dev 실행된다.
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "askdjango.settings") # settings 분기전
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "askdjango.settings.dev") # settings 폴더 생성후 분기
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
