from django.contrib.auth.models import User
from django.db import models

from settings import LANGUAGES


class Student(models.Model):
    user = models.OneToOneField(User)
    last_language_code = models.CharField(max_length=2, choices=LANGUAGES)

    def __str__(self):
        return self.user.username