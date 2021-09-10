#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

"""
    python manage.py runserver: サーバーを立ち上げ
    python manage.py (django-admin) migrate app_label migration_name: データベースの状態を現在のモデルやマイグレーションのセットと同期
    python manage.py (django-admin) makemigrations app_label: モデルに検出された変更点に基づいて、新しいマイグレーションを作成する。
    python manage.py createsuperuser: /adminにログインするためのアカウント作成
"""