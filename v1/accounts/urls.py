from django.urls import path, include
from rest_framework.routers import DefaultRouter

from v1.accounts.views.user import UserViewSet

router = DefaultRouter()
router.register(r'accounts', UserViewSet, base_name="account")

urlpatterns = [
    path(r'v1/', include(router.urls))
]
