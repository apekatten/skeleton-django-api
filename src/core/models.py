from auditlog.registry import auditlog
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pgp_pubkey = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{} {} ({})'.format(self.first_name, self.last_name, self.email)


auditlog.register(User)
