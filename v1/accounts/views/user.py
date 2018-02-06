from v1.accounts.models.user import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from v1.accounts.serializers.user import UserSerializer

# users
class UserView(APIView):

    @staticmethod
    def get(request):
        """
        List users
        """
        users = User.objects.all()
        return Response(UserSerializer(users, many=True).data)


class UserViewSet(ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

