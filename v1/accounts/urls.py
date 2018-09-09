from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token, verify_jwt_token

from v1.accounts.views.user import UserViewSet

router = DefaultRouter()
router.register(r'accounts', UserViewSet, base_name="account")

urlpatterns = [

    # Access Token
    path('token/', obtain_jwt_token, name="token"),
    path('token/verify', verify_jwt_token, name="token-verify"),
    path('token/refresh', refresh_jwt_token, name="token-refresh"),

    # V1
    path(r'v1/', include(router.urls))
]
