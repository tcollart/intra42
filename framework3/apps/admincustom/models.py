from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _


class MyLogEntry(models.Model):
    action_time = models.DateTimeField(_('action time'), auto_now=True)
    user = models.ForeignKey(User)
    message = models.TextField()

    def __str__(self):
        return "{date}: {user} {message}".format(date=self.action_time,
                                                 user=self.user,
                                                 message=self.message)