from v1.accounts.models.user import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.user.email
