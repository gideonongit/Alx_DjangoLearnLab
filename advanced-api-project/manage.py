#!/usr/bin/env python3
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advanced_api_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django.") from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

from api.models import Author, Book
from api.serializers import AuthorSerializer
a = Author.objects.first()
print(AuthorSerializer(a).data)

