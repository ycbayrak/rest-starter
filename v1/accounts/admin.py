from django.contrib import admin
from v1.accounts.models.profile import Profile
from v1.accounts.models.user import User


admin.site.register(Profile)
admin.site.register(User)
