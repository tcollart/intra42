from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from apps.students.models import Student


class Command(BaseCommand):
    help = 'Delete all students and users excluding user tcollart'

    def handle(self, *args, **options):
        Student.objects.all().delete()
        for user in User.objects.all():
            print(user)
            if user.id != 1:
                user.delete()
