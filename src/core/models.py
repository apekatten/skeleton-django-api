from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pgp_pubkey = models.TextField(blank=True)

    def __str__(self):
        return self.email
