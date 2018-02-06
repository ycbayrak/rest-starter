from v1.accounts.models.user import User
from v1.accounts.serializers.profile import ProfileSerializer
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
      model = User
      exclude = ('password',)
