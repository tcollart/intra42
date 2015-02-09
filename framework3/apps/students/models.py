from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    user = models.OneToOneField(User)
    birth_date = models.DateField(blank=True, null=True)
    picture = models.ImageField(blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    slug = models.SlugField(max_length=8, default=None, null=False, blank=False)

    def __str__(self):
        return self.user.username