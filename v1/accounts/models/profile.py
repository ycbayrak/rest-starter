from django.db import models

from v1.accounts.models.user import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.user.email
