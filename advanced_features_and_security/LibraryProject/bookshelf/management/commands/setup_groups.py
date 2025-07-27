from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from bookshelf.models import Document
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Set up groups and assign permissions'

    def handle(self, *args, **kwargs):
        content_type = ContentType.objects.get_for_model(Document)

        permissions = {
            'can_view': Permission.objects.get(codename='can_view', content_type=content_type),
            'can_create': Permission.objects.get(codename='can_create', content_type=content_type),
            'can_edit': Permission.objects.get(codename='can_edit', content_type=content_type),
            'can_delete': Permission.objects.get(codename='can_delete', content_type=content_type),
        }

        # Editors Group
        editors, _ = Group.objects.get_or_create(name='Editors')
        editors.permissions.set([permissions['can_create'], permissions['can_edit']])

        # Viewers Group
        viewers, _ = Group.objects.get_or_create(name='Viewers')
        viewers.permissions.set([permissions['can_view']])

        # Admins Group
        admins, _ = Group.objects.get_or_create(name='Admins')
        admins.permissions.set(permissions.values())

        self.stdout.write(self.style.SUCCESS('Groups and permissions set up successfully.'))
